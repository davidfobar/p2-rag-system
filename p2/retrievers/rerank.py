"""Your reranker (stage 1): ask Claude to reorder a first-stage system's top 20.

It is rerank_one() of the 13 lab's pipeline.py, moved onto the p2 interface:
- the first stage is hybrid (p2.retrievers.build, so its indexes are built once per run); its top 20
  documents (search) or top 20 chunks (search_chunks) are shown to Claude as numbered passages;
- for a document, the passage is the document's best chunk in hybrid's chunk ranking, because a
  document is long and the chunk is the part the first stage found for this query;
- one p2.claude.call per query, with a schema that forces {"order": [20 numbers]}, each from 1 to 20
  (minimum and maximum, so Claude cannot name a passage that does not exist);
- a reply that is not each number once, or a failed call, keeps the first-stage order;
- whatever hybrid ranks below the 20 stays underneath, in its own order.

The scores are made up from the final position (1 / position), because Claude gives an order and no
score; the run file only needs them to fall as the rank rises.
A reranker over 20 candidates is one call per query: 20 calls for the practice queries, 40 for the
test queries.
"""

from __future__ import annotations

from p2 import claude
from p2.corpus import docid_of
from p2.retrievers import build as build_system

NEEDS_CLAUDE = True

TOP = 20  # how many first-stage results Claude reorders

PROMPT = """You are ranking search results for a query.

Query: {query}

Below are {n} passages, numbered 1 to {n}. Rank them from most to least relevant to the query: the most \
relevant passage is the one that best answers or addresses the query. Reply with every number from 1 to {n} \
exactly once, best first.

{passages}
"""


def schema(n: int) -> dict:
    """The reply shape: {"order": [n numbers]}, each between 1 and n."""
    return {
        "type": "object",
        "properties": {
            "order": {
                "type": "array",
                "items": {"type": "integer", "minimum": 1, "maximum": n},
                "minItems": n,
                "maxItems": n,
            }
        },
        "required": ["order"],
    }


class Rerank:
    def __init__(self, corpus, cfg):
        self.corpus = corpus
        self.cfg = cfg
        self.model = cfg.model
        self.first = build_system("hybrid", corpus, cfg)
        self.chunk_text = {c.id: c.text for c in corpus.chunks(cfg.chunk_words, cfg.chunk_overlap)}
        self.n_chunks = len(self.chunk_text)

    def reorder(self, query: str, candidates: list[str], texts: list[str]) -> list[str]:
        """The candidates in Claude's order; the first-stage order when the reply is not usable."""
        n = len(candidates)
        if n < 2:
            return candidates
        passages = "\n\n".join(f"[{i}] {text}" for i, text in enumerate(texts, 1))
        reply = claude.call(
            PROMPT.format(query=query, n=n, passages=passages), schema(n),
            model=self.cfg.model, cache_dir=claude.cache_folder(self.cfg),
        )  # fmt: skip
        order = (reply.output or {}).get("order")
        if not isinstance(order, list) or sorted(order) != list(range(1, n + 1)):
            return candidates
        return [candidates[i - 1] for i in order]

    @staticmethod
    def scored(ids: list[str]) -> list[tuple[str, float]]:
        return [(item, 1 / rank) for rank, item in enumerate(ids, 1)]

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        first = [d for d, _ in self.first.search(text, max(k, TOP))]
        top = first[:TOP]
        best_chunk: dict[str, str] = {}
        for chunk_id, _ in self.first.search_chunks(text, self.n_chunks):
            best_chunk.setdefault(docid_of(chunk_id), self.chunk_text[chunk_id])
            if all(d in best_chunk for d in top):
                break
        # chunk 0 already starts with the "# title" line; a later chunk gets the title in front
        texts = [best_chunk.get(d, self.corpus.docs[d].text) for d in top]
        texts = [t if t.startswith("# ") else f"{self.corpus.docs[d].title}\n{t}" for d, t in zip(top, texts)]
        return self.scored(self.reorder(text, top, texts) + first[TOP:])[:k]

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        first = [c for c, _ in self.first.search_chunks(text, max(k, TOP))]
        top = first[:TOP]
        texts = [self.chunk_text[c] for c in top]
        return self.scored(self.reorder(text, top, texts) + first[TOP:])[:k]


def build(corpus, cfg):
    return Rerank(corpus, cfg)
