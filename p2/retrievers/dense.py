"""Dense retrieval (stage 1): embed every chunk once, embed the query, and rank chunks by cosine similarity.

It is the bge arm of the 12 lab's dense_rankings, moved from whole articles to chunks:
- the model is named in [dense] of p2.toml (model, bge-small-en-v1.5 by default) and loaded once
  through p2/embed.py;
- the chunk vectors are encoded once and cached in .cache/vectors/ by embed.doc_vectors;
- a query is encoded with [dense] query_prefix in front ("" by default, the lab's plain bge arm;
  the lab's stretch instruction is "Represent this sentence for searching relevant passages: ").

Every vector has length 1, so a chunk's score is the dot product of its vector and the query's,
and a document scores its best chunk (ChunkScorer).
"""

from __future__ import annotations

from p2 import embed
from p2.retrievers import ChunkScorer

NEEDS_CLAUDE = False


class Dense(ChunkScorer):
    def __init__(self, corpus, cfg):
        super().__init__(corpus, cfg)
        settings = cfg.table("dense")
        self.model = settings.get("model", embed.BGE)
        self.query_prefix = settings.get("query_prefix", "")
        self.embedder = embed.load(self.model)
        self.vectors = embed.doc_vectors(self.embedder, [c.text for c in self.chunks], cfg.root)

    def score_chunks(self, text: str) -> list[float]:
        if not self.chunks:
            return []
        query = self.embedder.encode([self.query_prefix + text])[0]
        return (self.vectors @ query).tolist()


def build(corpus, cfg):
    return Dense(corpus, cfg)
