"""Fetch Wikipedia articles from one or more categories into a folder that `p2 ingest` can read.

    uv run python scripts/fetch_wikipedia.py --category "Classical mechanics" --dry-run
    uv run python scripts/fetch_wikipedia.py --category "Classical mechanics" --out ../p2-raw

Standard library only. Wikipedia text is CC BY-SA 4.0; each file is named after the article's URL title,
so `p2 ingest ... --source "https://en.wikipedia.org/wiki/{stem}"` gives every document its own address.
The revision id of every file is recorded in sources.tsv beside the files.
"""

import argparse
import json
import random
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://en.wikipedia.org/w/api.php"
AGENT = "csci498e-p2-corpus-builder/0.1 (student course project; david.fobar@gmail.com)"
PAUSE = 0.3  # seconds between requests
DROP_SECTIONS = {"references", "external links", "see also", "further reading", "notes", "bibliography",
                 "footnotes", "sources", "citations"}


def api(**params) -> dict:
    url = API + "?" + urllib.parse.urlencode({"format": "json", "formatversion": "2", **params})
    request = urllib.request.Request(url, headers={"User-Agent": AGENT})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                data = json.load(response)
            time.sleep(PAUSE)
            return data
        except OSError:
            time.sleep(2 * (attempt + 1))
    sys.exit(f"Wikipedia did not answer after 4 tries: {url}")


def members(category: str, kind: str) -> list[str]:
    """Titles of the pages (kind 'page') or subcategories (kind 'subcat') directly in a category."""
    titles, token = [], {}
    while True:
        data = api(action="query", list="categorymembers", cmtitle=f"Category:{category}", cmtype=kind,
                   cmnamespace="14" if kind == "subcat" else "0", cmlimit="500", **token)
        titles += [m["title"] for m in data["query"]["categorymembers"]]
        if "continue" not in data:
            return titles
        token = {"cmcontinue": data["continue"]["cmcontinue"]}


def collect(categories: list[str], depth: int) -> list[str]:
    """Article titles in the categories and their subcategories down to `depth`, in the order found."""
    seen_categories, found, frontier = set(categories), {}, [(c, 0) for c in categories]
    while frontier:
        category, level = frontier.pop(0)
        for title in members(category, "page"):
            found.setdefault(title, None)
        if level < depth:
            for sub in members(category, "subcat"):
                name = sub.removeprefix("Category:")
                if name not in seen_categories:
                    seen_categories.add(name)
                    frontier.append((name, level + 1))
        print(f"  category {category!r} (depth {level}): {len(found)} articles so far", file=sys.stderr)
    return list(found)


def fetch(title: str) -> tuple[str, int, str] | None:
    """(canonical title, revision id, plain text) of an article, or None when it is not an article."""
    data = api(action="query", titles=title, redirects="1", prop="extracts|revisions", explaintext="1",
               exsectionformat="wiki", rvprop="ids")
    page = data["query"]["pages"][0]
    if page.get("missing") or "extract" not in page:
        return None
    return page["title"], page["revisions"][0]["revid"], page["extract"]


def clean(title: str, text: str) -> str:
    """Markdown with `## Heading` lines and the closing reference-type sections removed."""
    out, skipping = [], False
    for line in text.splitlines():
        heading = re.fullmatch(r"(=+)\s*(.*?)\s*\1", line.strip())
        if heading:
            level, name = len(heading.group(1)), heading.group(2)
            if level == 2:
                skipping = name.lower() in DROP_SECTIONS
            if not skipping:
                out.append("#" * level + " " + name)
        elif not skipping:
            out.append(line)
    body = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()
    return f"# {title}\n\n{body}\n"


def filename(title: str) -> str:
    return title.replace(" ", "_").replace("/", "_")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--category", action="append", required=True, help="a category name; repeatable")
    parser.add_argument("--depth", type=int, default=1, help="how many levels of subcategories to follow (default 1)")
    parser.add_argument("--min-words", type=int, default=500, help="skip shorter articles (default 500)")
    parser.add_argument("--max-words", type=int, default=6000, help="skip longer articles (default 6000)")
    parser.add_argument("--budget-words", type=int, default=600000, help="stop after this many words (default 600000)")
    parser.add_argument("--seed", type=int, default=0, help="seed for the shuffle of candidate titles (default 0)")
    parser.add_argument("--out", default="../p2-raw", help="folder for the .md files (default ../p2-raw)")
    parser.add_argument("--dry-run", action="store_true", help="fetch and count, but write nothing")
    parser.add_argument("--limit", type=int, default=0, help="look at only the first N titles (for a trial)")
    args = parser.parse_args()

    print("Listing categories...", file=sys.stderr)
    titles = collect(args.category, args.depth)
    random.Random(args.seed).shuffle(titles)  # so a word budget samples every category, not the first ones
    if args.limit:
        titles = titles[: args.limit]
    print(f"{len(titles)} candidate titles; fetching text...", file=sys.stderr)

    out = Path(args.out)
    kept, words_total, skipped = [], 0, {"short": 0, "long": 0, "missing": 0, "duplicate": 0}
    names = set()
    for i, title in enumerate(titles, 1):
        got = fetch(title)
        if got is None:
            skipped["missing"] += 1
            continue
        canonical, revid, text = got
        if canonical in names:  # two titles that redirect to one article
            skipped["duplicate"] += 1
            continue
        body = clean(canonical, text)
        words = len(body.split())
        if words < args.min_words:
            skipped["short"] += 1
        elif words > args.max_words:
            skipped["long"] += 1
        elif words_total + words > args.budget_words:
            print(f"Word budget {args.budget_words} reached at article {i}.", file=sys.stderr)
            break
        else:
            names.add(canonical)
            kept.append((canonical, revid, words, body))
            words_total += words
        if i % 25 == 0:
            print(f"  {i}/{len(titles)} looked at, {len(kept)} kept, {words_total} words", file=sys.stderr)

    print(f"\nKept {len(kept)} articles, {words_total} words (about {int(words_total * 1.4)} tokens).")
    print(f"Skipped: {skipped}")
    if kept:
        words = sorted(w for _, _, w, _ in kept)
        print(f"Words per article: min {words[0]}, median {words[len(words) // 2]}, max {words[-1]}")
    if args.dry_run:
        for title, _, w, _ in kept:
            print(f"{w:6d}  {title}")
        print("\nDry run: nothing written.")
        return

    out.mkdir(parents=True, exist_ok=True)
    rows = ["file\turl\trevid"]
    for title, revid, _, body in kept:
        (out / f"{filename(title)}.md").write_text(body, encoding="utf-8", newline="\n")
        rows.append(f"{filename(title)}.md\thttps://en.wikipedia.org/wiki/{urllib.parse.quote(title.replace(' ', '_'))}\t{revid}")
    (out / "sources.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
    print(f"Wrote {len(kept)} files and sources.tsv to {out}")


if __name__ == "__main__":
    main()
