"""Hybrid retrieval (stage 1): fuse the full rankings of two systems with reciprocal rank fusion.

It is rrf() from the 13 lab's pipeline.py, moved onto the p2 interface:
- the two systems are named in [hybrid] of p2.toml (systems, ["bm25", "dense"] by default) and
  built through p2.retrievers.build, so each index is built once per run;
- each system ranks every document (or every chunk, for search_chunks), not just its top 10,
  because a document that is 11th in both lists can belong in the fused top 10;
- a document scores the sum of 1 / (rrf_k + rank) over the two rankings, ranks from 1, with
  rrf_k from [hybrid] (60 by default, the lab's value).

The fused scores are ordered with p2.runfile.order, so equal scores fall in document id order.
"""

from __future__ import annotations

from collections import defaultdict

from p2.retrievers import build as build_system
from p2.runfile import order

NEEDS_CLAUDE = False


def rrf(rankings, k=60):
    """Reciprocal rank fusion of rankings of (id, score) pairs, best first: id -> fused score."""
    scores: dict[str, float] = defaultdict(float)
    for ranking in rankings:
        for rank, (item, _score) in enumerate(ranking, 1):
            scores[item] += 1 / (k + rank)
    return scores


class Hybrid:
    def __init__(self, corpus, cfg):
        settings = cfg.table("hybrid")
        self.names = list(settings.get("systems", ["bm25", "dense"]))
        self.rrf_k = settings.get("rrf_k", 60)
        self.systems = [build_system(name, corpus, cfg) for name in self.names]
        self.n_docs = len(corpus.docs)
        self.n_chunks = len(corpus.chunks(cfg.chunk_words, cfg.chunk_overlap))

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        rankings = [s.search(text, self.n_docs) for s in self.systems]
        return order(rrf(rankings, self.rrf_k).items())[:k]

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        rankings = [s.search_chunks(text, self.n_chunks) for s in self.systems]
        return order(rrf(rankings, self.rrf_k).items())[:k]


def build(corpus, cfg):
    return Hybrid(corpus, cfg)
