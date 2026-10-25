"""Ablation of hybrid: the same reciprocal rank fusion, with the dense ranking counted more than bm25.

Everything else is hybrid's: the two systems and rrf_k from [hybrid] of p2.toml, and each system
ranking every document (or chunk). The one change is a weight on each ranking, so a document scores
the sum of weight / (rrf_k + rank); with WEIGHTS below, a dense rank counts twice a bm25 rank.
"""

from __future__ import annotations

from collections import defaultdict

from p2.retrievers.hybrid import Hybrid
from p2.runfile import order

NEEDS_CLAUDE = False

BASE = "hybrid"

WEIGHTS = {"bm25": 1.0, "dense": 2.0}  # a system not named here counts 1


def weighted_rrf(rankings, weights, k=60):
    """Reciprocal rank fusion with a weight per ranking: id -> fused score."""
    scores: dict[str, float] = defaultdict(float)
    for ranking, weight in zip(rankings, weights):
        for rank, (item, _score) in enumerate(ranking, 1):
            scores[item] += weight / (k + rank)
    return scores


class WeightedHybrid(Hybrid):
    def __init__(self, corpus, cfg):
        super().__init__(corpus, cfg)
        self.weights = [WEIGHTS.get(name, 1.0) for name in self.names]

    def search(self, text: str, k: int) -> list[tuple[str, float]]:
        rankings = [s.search(text, self.n_docs) for s in self.systems]
        return order(weighted_rrf(rankings, self.weights, self.rrf_k).items())[:k]

    def search_chunks(self, text: str, k: int) -> list[tuple[str, float]]:
        rankings = [s.search_chunks(text, self.n_chunks) for s in self.systems]
        return order(weighted_rrf(rankings, self.weights, self.rrf_k).items())[:k]


def build(corpus, cfg):
    return WeightedHybrid(corpus, cfg)
