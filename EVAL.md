# Evaluation report

This is the report on what you built and what the numbers let you claim.
Two kinds of text live here.

The tables between a `p2:begin` comment line and its matching `p2:end` comment line are written by `uv run p2 score` from your committed run files and answers files.
Please do not edit anything between those two lines, because `uv run p2 check` recomputes them and fails when they differ.
A table that says no runs or answers exist yet is waiting for data; run `uv run p2 score` after you commit the files it needs.

Everything else is yours.
Each prompt ends with a marker line that you replace with your own writing; `uv run p2 check --final` fails while one is left.
Write what you measured, including what did not work.
What I read for is whether each claim matches its interval, not whether the result is good news.

Words used below: recall@10, MRR@10 and nDCG@10 are the three scores, each averaged over the queries of a set; step 7 of stage 1 in the README defines them, and lecture 14 goes deeper.
A paired interval is the 95% interval of the mean difference between two systems on the same queries, found by resampling the queries 10,000 times.
When an interval includes zero, the gold set cannot tell the two systems apart, and the right words are "not distinguishable on this gold set".
The minimum detectable difference is the smallest gap this many queries could reliably show, so a difference below it is invisible to this gold set, not absent.

---

## 1. Stage 1 - the shared corpus (30 CFR Chapter I)

### What you built

For each of `dense`, `hybrid` and `rerank`, one or two sentences: the embedding model, how documents were chunked, what was fused and how, how many candidates the reranker saw, and anything you changed from the 12 and 13 lab code.

Dense: the bge-small-en-v1.5 embedding model is used with cosine similarity for vector comparison.
Hybrid: fuses bm25 and dense with a reciprocal rank fusion. This means that similar rankings get more weight than vastly different rankings.
rerank: get top 20 using hybrd, pass all 20 queries and hybrid results. The reply is restricted to a set of integers that provides the LLM rankings.

### Practice queries (20)

Scores per system.

<!-- p2:begin shared-practice -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.625 | 0.507 | 0.518 |
| dense | 0.558 | 0.562 | 0.480 |
| hybrid | 0.592 | 0.471 | 0.444 |
| rerank | 0.758 | 0.800 | 0.769 |

20 judged queries; nDCG uses binary labels; a random ranking of the 2,484 documents would get recall@10 near 0.004.
<!-- p2:end shared-practice -->

The same scores per query class.

<!-- p2:begin shared-practice-classes -->
| System | Metric | identifier (n=7) | paraphrase (n=7) | mixed (n=6) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 1.000 | 0.000 | 0.917 |
| bm25 | MRR@10 | 0.810 | 0.000 | 0.746 |
| bm25 | nDCG@10 | 0.857 | 0.000 | 0.728 |
| dense | Recall@10 | 0.214 | 0.595 | 0.917 |
| dense | MRR@10 | 0.333 | 0.714 | 0.653 |
| dense | nDCG@10 | 0.211 | 0.593 | 0.661 |
| hybrid | Recall@10 | 0.500 | 0.405 | 0.917 |
| hybrid | MRR@10 | 0.514 | 0.154 | 0.792 |
| hybrid | nDCG@10 | 0.397 | 0.203 | 0.779 |
| rerank | Recall@10 | 0.714 | 0.595 | 1.000 |
| rerank | MRR@10 | 0.714 | 0.714 | 1.000 |
| rerank | nDCG@10 | 0.714 | 0.626 | 1.000 |
<!-- p2:end shared-practice-classes -->

Differences between every pair of systems, each with its paired interval and the minimum detectable difference.

<!-- p2:begin shared-practice-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | -0.067 | [-0.350, +0.225] | 0.415 | not distinguishable |
| dense minus bm25 | MRR@10 | +0.055 | [-0.225, +0.343] | 0.412 | not distinguishable |
| dense minus bm25 | nDCG@10 | -0.039 | [-0.302, +0.231] | 0.385 | not distinguishable |
| hybrid minus bm25 | Recall@10 | -0.033 | [-0.250, +0.192] | 0.324 | not distinguishable |
| hybrid minus bm25 | MRR@10 | -0.036 | [-0.178, +0.084] | 0.193 | not distinguishable |
| hybrid minus bm25 | nDCG@10 | -0.075 | [-0.238, +0.075] | 0.228 | not distinguishable |
| hybrid minus dense | Recall@10 | +0.033 | [-0.125, +0.192] | 0.231 | not distinguishable |
| hybrid minus dense | MRR@10 | -0.091 | [-0.305, +0.110] | 0.300 | not distinguishable |
| hybrid minus dense | nDCG@10 | -0.036 | [-0.199, +0.113] | 0.227 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.133 | [-0.100, +0.358] | 0.340 | not distinguishable |
| rerank minus bm25 | MRR@10 | +0.293 | [+0.043, +0.533] | 0.353 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.251 | [+0.022, +0.466] | 0.323 | rerank higher |
| rerank minus dense | Recall@10 | +0.200 | [+0.050, +0.367] | 0.224 | rerank higher |
| rerank minus dense | MRR@10 | +0.237 | [+0.083, +0.408] | 0.239 | rerank higher |
| rerank minus dense | nDCG@10 | +0.289 | [+0.149, +0.443] | 0.214 | rerank higher |
| rerank minus hybrid | Recall@10 | +0.167 | [+0.058, +0.292] | 0.166 | rerank higher |
| rerank minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | 0.246 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.325 | [+0.199, +0.453] | 0.184 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end shared-practice-pairs -->

The 40 test queries have no answer key in this repo.
Your test run files are scored by the course and the score comes back to you as feedback, so nothing goes here for them.

### What the intervals let you claim

Which differences are distinguishable from zero and which are not?
What is the minimum detectable difference at 20 queries, and what does that say about any gap smaller than it?
Which claim from lecture 12 or 13 did your numbers support, and which did they leave open?

That the rerank provides meaningful utility to a RAG system

---

## 2. Stage 1 - cited answers on the 12 shared questions

<!-- p2:begin answers -->
| Label | System | Verified (in) | 95% interval | not_found (in) | Declined (out) | 95% interval | Quotes found |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| dense | dense | 1 of 3 (33%) | [0.061, 0.792] | 2 of 3 (67%) | 1 of 1 (100%) | [0.207, 1.000] | 5 of 5 |
| rerank | rerank | 8 of 8 (100%) | [0.676, 1.000] | 0 of 8 (0%) | 4 of 4 (100%) | [0.510, 1.000] | 13 of 13 |
<!-- p2:end answers -->

Which system answered, and why that one?
What did you change in `prompts/answer.txt`, if anything, and did the verified share or the declined share move?

Then read three in-corpus answers that `uv run p2 verify` passed.
For each one, open the cited chunk and say whether the quote really supports the claim next to it.
The check proves a quote is a real piece of the chunk and cannot prove that it supports the claim, so this reading is the part only you can do.

As far as I can tell (without being a mining expert), it would seem like the LLM/RAG successfully quotes correct documents.

---

## 3. Stage 2 - your corpus and your gold set

### The corpus

What is it, where did it come from, how many documents and how many megabytes, and what is the license basis for publishing it?
Name the one or two documents you were least sure about and what you decided.
Say which of the allowed sources in the brief it comes from.

I used Wikipedia since the OpenStax license was not acceptable. Wikipedia maintains a CC BY-SA license.

### The gold set

How many queries, how many with origin `hand` and how many with origin `claude`, and which query classes did you use and why?
How did you decide that a document is relevant: write your relevance rule in two or three sentences, the way the brief does for the shared corpus.
How did you find candidates (the systems' top 10, a keyword search, reading), and did you read every document before you labeled it?
Your labels are binary (`rel` 1) unless you say otherwise: if you use graded labels, declare the scale here, for example 2 means the document answers the query fully and 1 means it helps.

I made a list of 40 queries, each best supported by a specific document in the corpora. I based the relivance from my experience teaching undergradtuate physics.

---

## 4. Stage 2 - results on your corpus

Scores per system on your gold set.

<!-- p2:begin own -->
| System | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| bm25 | 0.875 | 0.657 | 0.709 |
| dense | 1.000 | 0.831 | 0.873 |
| hybrid | 0.950 | 0.751 | 0.800 |
| rerank | 1.000 | 0.869 | 0.901 |
| ablation/hybrid_dense | 0.975 | 0.760 | 0.812 |

40 judged queries; nDCG uses binary labels; a random ranking of the 249 documents would get recall@10 near 0.040.
<!-- p2:end own -->

The same scores per query class.

<!-- p2:begin own-classes -->
| System | Metric | identifier (n=7) | paraphrase (n=24) | mixed (n=9) |
| --- | --- | ---: | ---: | ---: |
| bm25 | Recall@10 | 0.857 | 0.875 | 0.889 |
| bm25 | MRR@10 | 0.786 | 0.588 | 0.741 |
| bm25 | nDCG@10 | 0.804 | 0.656 | 0.776 |
| dense | Recall@10 | 1.000 | 1.000 | 1.000 |
| dense | MRR@10 | 0.804 | 0.817 | 0.889 |
| dense | nDCG@10 | 0.849 | 0.862 | 0.918 |
| hybrid | Recall@10 | 0.857 | 0.958 | 1.000 |
| hybrid | MRR@10 | 0.714 | 0.731 | 0.833 |
| hybrid | nDCG@10 | 0.752 | 0.786 | 0.873 |
| rerank | Recall@10 | 1.000 | 1.000 | 1.000 |
| rerank | MRR@10 | 0.893 | 0.872 | 0.843 |
| rerank | nDCG@10 | 0.919 | 0.903 | 0.881 |
| ablation/hybrid_dense | Recall@10 | 0.857 | 1.000 | 1.000 |
| ablation/hybrid_dense | MRR@10 | 0.690 | 0.774 | 0.778 |
| ablation/hybrid_dense | nDCG@10 | 0.733 | 0.828 | 0.832 |
<!-- p2:end own-classes -->

The same scores for the queries you wrote yourself (`hand`) and the ones a model drafted (`claude`), with the difference between the two groups and its interval.
Once both groups have queries, the table also says whether `bm25`'s lead over `dense` differs between them, and what share of each query's content words its best relevant document contains, which is stretch option 6.

<!-- p2:begin own-origins -->
| System | Metric | hand (n=12) | claude (n=28) | hand minus claude | 95% interval | Reading |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| bm25 | Recall@10 | 0.750 | 0.929 | -0.179 | [-0.464, +0.060] | not distinguishable |
| bm25 | MRR@10 | 0.476 | 0.735 | -0.259 | [-0.528, +0.013] | not distinguishable |
| bm25 | nDCG@10 | 0.540 | 0.781 | -0.241 | [-0.493, +0.008] | not distinguishable |
| dense | Recall@10 | 1.000 | 1.000 | +0.000 | [+0.000, +0.000] | not distinguishable |
| dense | MRR@10 | 0.624 | 0.920 | -0.295 | [-0.506, -0.086] | claude higher |
| dense | nDCG@10 | 0.715 | 0.940 | -0.225 | [-0.387, -0.066] | claude higher |
| hybrid | Recall@10 | 0.917 | 0.964 | -0.048 | [-0.250, +0.107] | not distinguishable |
| hybrid | MRR@10 | 0.531 | 0.845 | -0.314 | [-0.548, -0.077] | claude higher |
| hybrid | nDCG@10 | 0.625 | 0.875 | -0.250 | [-0.453, -0.050] | claude higher |
| rerank | Recall@10 | 1.000 | 1.000 | +0.000 | [+0.000, +0.000] | not distinguishable |
| rerank | MRR@10 | 0.764 | 0.914 | -0.150 | [-0.364, +0.048] | not distinguishable |
| rerank | nDCG@10 | 0.821 | 0.935 | -0.115 | [-0.278, +0.035] | not distinguishable |
| ablation/hybrid_dense | Recall@10 | 0.917 | 1.000 | -0.083 | [-0.250, +0.000] | not distinguishable |
| ablation/hybrid_dense | MRR@10 | 0.540 | 0.855 | -0.315 | [-0.544, -0.086] | claude higher |
| ablation/hybrid_dense | nDCG@10 | 0.632 | 0.890 | -0.257 | [-0.457, -0.070] | claude higher |

The hand and claude queries are different queries, so the interval of hand minus claude comes from resampling the queries within each group (10,000 times), not from pairing them.

Do model-written queries favor keyword search? bm25's lead over dense (bm25 minus dense, per query) on the claude queries and on the hand queries, and claude minus hand:

| Metric | Lead on claude | Lead on hand | Claude minus hand | 95% interval | Reading |
| --- | ---: | ---: | ---: | ---: | --- |
| Recall@10 | -0.071 | -0.250 | +0.179 | [-0.071, +0.464] | not distinguishable |
| MRR@10 | -0.185 | -0.148 | -0.036 | [-0.354, +0.280] | not distinguishable |
| nDCG@10 | -0.159 | -0.175 | +0.016 | [-0.270, +0.311] | not distinguishable |

Mean content-word overlap, the share of a query's content words found in its best relevant document: hand 0.79 (12 queries), claude 0.81 (28 queries).

Stretch option 6 asks for at least 20 judged queries of each origin; here there are 12 hand and 28 claude.
<!-- p2:end own-origins -->

Differences between every pair of systems.

<!-- p2:begin own-pairs -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| dense minus bm25 | Recall@10 | +0.125 | [+0.025, +0.225] | 0.148 | dense higher |
| dense minus bm25 | MRR@10 | +0.174 | [+0.052, +0.298] | 0.180 | dense higher |
| dense minus bm25 | nDCG@10 | +0.164 | [+0.058, +0.276] | 0.160 | dense higher |
| hybrid minus bm25 | Recall@10 | +0.075 | [+0.000, +0.175] | 0.118 | not distinguishable |
| hybrid minus bm25 | MRR@10 | +0.094 | [+0.032, +0.159] | 0.093 | hybrid higher |
| hybrid minus bm25 | nDCG@10 | +0.090 | [+0.038, +0.147] | 0.080 | hybrid higher |
| hybrid minus dense | Recall@10 | -0.050 | [-0.125, +0.000] | 0.098 | not distinguishable |
| hybrid minus dense | MRR@10 | -0.080 | [-0.183, +0.011] | 0.141 | not distinguishable |
| hybrid minus dense | nDCG@10 | -0.073 | [-0.165, +0.006] | 0.124 | not distinguishable |
| rerank minus bm25 | Recall@10 | +0.125 | [+0.025, +0.225] | 0.148 | rerank higher |
| rerank minus bm25 | MRR@10 | +0.212 | [+0.095, +0.328] | 0.170 | rerank higher |
| rerank minus bm25 | nDCG@10 | +0.192 | [+0.094, +0.292] | 0.145 | rerank higher |
| rerank minus dense | Recall@10 | +0.000 | [+0.000, +0.000] | - | identical on every query |
| rerank minus dense | MRR@10 | +0.038 | [-0.074, +0.151] | 0.164 | not distinguishable |
| rerank minus dense | nDCG@10 | +0.028 | [-0.056, +0.114] | 0.124 | not distinguishable |
| rerank minus hybrid | Recall@10 | +0.050 | [+0.000, +0.125] | 0.098 | not distinguishable |
| rerank minus hybrid | MRR@10 | +0.118 | [+0.013, +0.230] | 0.156 | rerank higher |
| rerank minus hybrid | nDCG@10 | +0.101 | [+0.016, +0.194] | 0.128 | rerank higher |
| ablation/hybrid_dense minus bm25 | Recall@10 | +0.100 | [+0.025, +0.200] | 0.135 | ablation/hybrid_dense higher |
| ablation/hybrid_dense minus bm25 | MRR@10 | +0.103 | [+0.020, +0.185] | 0.119 | ablation/hybrid_dense higher |
| ablation/hybrid_dense minus bm25 | nDCG@10 | +0.103 | [+0.035, +0.174] | 0.101 | ablation/hybrid_dense higher |
| ablation/hybrid_dense minus dense | Recall@10 | -0.025 | [-0.075, +0.000] | 0.070 | not distinguishable |
| ablation/hybrid_dense minus dense | MRR@10 | -0.071 | [-0.161, +0.004] | 0.118 | not distinguishable |
| ablation/hybrid_dense minus dense | nDCG@10 | -0.060 | [-0.138, +0.002] | 0.101 | not distinguishable |
| ablation/hybrid_dense minus hybrid | Recall@10 | +0.025 | [+0.000, +0.075] | 0.070 | not distinguishable |
| ablation/hybrid_dense minus hybrid | MRR@10 | +0.009 | [-0.033, +0.055] | 0.062 | not distinguishable |
| ablation/hybrid_dense minus hybrid | nDCG@10 | +0.013 | [-0.021, +0.050] | 0.050 | not distinguishable |
| ablation/hybrid_dense minus rerank | Recall@10 | -0.025 | [-0.075, +0.000] | 0.070 | not distinguishable |
| ablation/hybrid_dense minus rerank | MRR@10 | -0.109 | [-0.217, -0.005] | 0.153 | rerank higher |
| ablation/hybrid_dense minus rerank | nDCG@10 | -0.089 | [-0.173, -0.009] | 0.119 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time. Two systems that score the same on every query have no interval to speak of, so their MDD is shown as -.
<!-- p2:end own-pairs -->

Which differences are distinguishable and which are not, at your gold-set size?
Do the `hand` queries and the `claude` queries tell the same story?
Did your prediction in `DECISIONS.md` prompt 1 hold?

With this contect, dense is able to perform as well as rerank, but in general adding rerank to the system does improve if tokens are available. The claude generated prompts do slighlty out perform the hand generated ones, specifically when the dense model is being used.

---

## 5. The ablation

Change one thing and keep everything else the same.
Write your hypothesis here before you run it, in one sentence with a direction: "I expect X to raise MRR@10 on my corpus because Y."
The run file for it lives in `runs/own/ablation/`.

<!-- p2:begin own-ablation -->
| Comparison | Metric | Mean difference | 95% interval | MDD | Reading |
| --- | --- | ---: | ---: | ---: | --- |
| ablation/hybrid_dense minus bm25 | Recall@10 | +0.100 | [+0.025, +0.200] | 0.135 | ablation/hybrid_dense higher |
| ablation/hybrid_dense minus bm25 | MRR@10 | +0.103 | [+0.020, +0.185] | 0.119 | ablation/hybrid_dense higher |
| ablation/hybrid_dense minus bm25 | nDCG@10 | +0.103 | [+0.035, +0.174] | 0.101 | ablation/hybrid_dense higher |
| ablation/hybrid_dense minus dense | Recall@10 | -0.025 | [-0.075, +0.000] | 0.070 | not distinguishable |
| ablation/hybrid_dense minus dense | MRR@10 | -0.071 | [-0.161, +0.004] | 0.118 | not distinguishable |
| ablation/hybrid_dense minus dense | nDCG@10 | -0.060 | [-0.138, +0.002] | 0.101 | not distinguishable |
| ablation/hybrid_dense minus hybrid | Recall@10 | +0.025 | [+0.000, +0.075] | 0.070 | not distinguishable |
| ablation/hybrid_dense minus hybrid | MRR@10 | +0.009 | [-0.033, +0.055] | 0.062 | not distinguishable |
| ablation/hybrid_dense minus hybrid | nDCG@10 | +0.013 | [-0.021, +0.050] | 0.050 | not distinguishable |
| ablation/hybrid_dense minus rerank | Recall@10 | -0.025 | [-0.075, +0.000] | 0.070 | not distinguishable |
| ablation/hybrid_dense minus rerank | MRR@10 | -0.109 | [-0.217, -0.005] | 0.153 | rerank higher |
| ablation/hybrid_dense minus rerank | nDCG@10 | -0.089 | [-0.173, -0.009] | 0.119 | rerank higher |

The interval is a paired bootstrap (10,000 resamples of the queries); MDD is the smallest difference this many queries detect 80% of the time.
<!-- p2:end own-ablation -->

The queries your ablation helped and hurt, against the system it varies, by reciprocal rank.
`p2 score` finds that system from a line such as `BASE = "bm25"` in your variant's file, or else from its name: `bm25_lab` varies `bm25`.

<!-- p2:begin own-ablation-queries -->
ablation/hybrid_dense against hybrid (BASE = "hybrid" in p2/retrievers/hybrid_dense.py): it helped 5 queries, hurt 2 and left 33 unchanged.

| Query | Class | Origin | hybrid RR | ablation/hybrid_dense RR | Change | Effect |
| --- | --- | --- | ---: | ---: | ---: | --- |
| c16 | paraphrase | claude | 0.333 | 1.000 | +0.667 | helped |
| c33 | paraphrase | hand | 0.333 | 0.500 | +0.167 | helped |
| c19 | paraphrase | claude | 0.000 | 0.100 | +0.100 | helped |
| c36 | paraphrase | hand | 0.167 | 0.250 | +0.083 | helped |
| c39 | paraphrase | hand | 0.125 | 0.143 | +0.018 | helped |
| c27 | mixed | claude | 1.000 | 0.500 | -0.500 | hurt |
| c30 | identifier | hand | 0.500 | 0.333 | -0.167 | hurt |

RR is the reciprocal rank of the first relevant document in the top 10 (0 when none is there), the per-query value behind MRR@10; the queries at the top of each list are the ones to read.
<!-- p2:end own-ablation-queries -->

What did you change, what happened, and does the interval support the claim you want to make?
If the result is not distinguishable, say what size of effect your gold set could have seen.
Read the queries at the top of each list in the second table, and say whether your change explains them.

Given that dense is highly accurate, outperforming the hybrid model, I will change the hybrid model to place more weight in the dense model while still taking into account bm25. I expect the hybrid results to improve as a result of the change, which can have downstream impacts to rerank as well.

Using the table, the queries that were helped were more indirect questions. The ones that were hurt have valid information about the topic in the referenced docuements, but the number one document was not the best one.

---

## 6. Failure analysis

Pick the queries where your best system on your own corpus failed: the relevant document is missing from the top 10, or sits far below the top.
Take at least five, and read what the system returned next to what was relevant.
Then sort the failures by cause, for example a vocabulary mismatch, near-duplicate documents, a chunk that cut the answer in half, a query that is ambiguous, or a label that was wrong, because sometimes the gold set is what failed.

| qid | what the best system returned | what was relevant | cause | what you would try |
|---|---|---|---|---|

TODO: add one row for each failure you analyzed, and write two or three sentences on the pattern you see across them.

---

## 7. Cross-corpus comparison

The two tables to compare are the shared-corpus scores in section 1 and your own-corpus scores in section 4, with their intervals.
If you want them side by side, copy the rows you need into a table here and say that you copied them.

Did the winner change between the shared corpus and yours?
Why, or why not: what is different about the two collections (document length, vocabulary, identifiers, near-duplicates, how the queries were written), and which of your explanations did you test and which are guesses?
Say what 20 queries on one side and your gold-set size on the other cannot support.

TODO: write the cross-corpus comparison.

---

## 8. Stretch

498E: the stretch is one of the six options in the brief's "One stretch" section, and that section says what earns the 25 points for each.
It is optional, so `uv run p2 check --final` never waits on this section.
598E: the rider is your stretch, so write "rider" below and put its results in section 9; the other options add no points, because the project is capped at 150.

Whichever option you chose, write these five things:

1. The option's name.
2. What you did, and the files that hold it.
3. The table `p2 score` wrote for it, by name: one of the three below, `own-ablation` and `own-ablation-queries` in section 5 for a second ablation, `own-origins` in section 4 for the hand and claude queries, or `repeats` in section 9 for the rider.
4. What its interval lets you claim, and what it does not.
5. One thing you would do next, and what result would tell you it worked.

For a second ablation, write its hypothesis here before you run it, and commit it, so your history shows that it came first.
For the hand and claude queries, do the same with your prediction before you score.

### Claim-level faithfulness check (option 2)

Claude's verdicts from `p2 judge` against your own verdicts in the calibration file.

<!-- p2:begin stretch-judge -->
_No judged answers yet (stretch option 2): `uv run p2 judge answers/shared/LABEL.json` writes them, your own verdicts go in answers/shared/LABEL.calibration.tsv, and then `uv run p2 score` fills this table._
<!-- p2:end stretch-judge -->

### Cost and latency (option 3)

The Claude calls, tokens and seconds in every trace you committed, and what a cheaper system or answers file saves against what it loses.

<!-- p2:begin stretch-cost -->
Every trace in traces/ that records a Claude call:

| Trace | System | Spans | Claude calls | Saved | Input tokens | Output tokens | Seconds | Input per span | Output per span | Seconds per span |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| traces/answers-dense.jsonl | dense | 4 | 4 | 3 | 22,387 | 1,821 | 23.8 | 5,597 | 455 | 6.0 |
| traces/answers-rerank.jsonl | rerank | 12 | 24 | 0 | 200,752 | 4,314 | 78.2 | 16,729 | 360 | 6.5 |
| traces/answers-rerank.r1.jsonl | rerank | 12 | 24 | 0 | 208,898 | 4,048 | 85.3 | 17,408 | 337 | 7.1 |
| traces/answers-rerank.r2.jsonl | rerank | 12 | 24 | 0 | 211,375 | 4,563 | 80.3 | 17,615 | 380 | 6.7 |
| traces/answers-rerank.r3.jsonl | rerank | 12 | 24 | 0 | 204,817 | 4,204 | 76.0 | 17,068 | 350 | 6.3 |
| traces/own-own-rerank.jsonl | rerank | 40 | 40 | 0 | 718,434 | 3,762 | 119.8 | 17,961 | 94 | 3.0 |
| traces/shared-practice-rerank.jsonl | rerank | 20 | 20 | 20 | 275,629 | 1,930 | 66.8 | 13,781 | 96 | 3.3 |
| traces/shared-practice-rerank.r1.jsonl | rerank | 20 | 20 | 0 | 284,563 | 2,040 | 60.5 | 14,228 | 102 | 3.0 |
| traces/shared-practice-rerank.r2.jsonl | rerank | 20 | 20 | 0 | 247,028 | 2,051 | 58.3 | 12,351 | 103 | 2.9 |
| traces/shared-practice-rerank.r3.jsonl | rerank | 20 | 20 | 0 | 247,028 | 2,020 | 55.6 | 12,351 | 101 | 2.8 |
| traces/shared-test-rerank.jsonl | rerank | 40 | 40 | 0 | 524,056 | 3,860 | 129.4 | 13,101 | 96 | 3.2 |

A span is one query of a run, one question of an answers file, or one claim of a judged file. A saved reply costs nothing now, so it counts the tokens and the seconds of the call that made it.

Every pair of systems on the same queries where at least one calls Claude, the one with fewer Claude input tokens per query first:

| Cheaper minus dearer | Queries | MRR@10 difference | 95% interval | Input tokens saved per query | Seconds saved per query | Reading |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| shared practice: bm25 minus rerank | 20 | -0.293 | [-0.533, -0.043] | 13,781 | 3.3 | rerank higher |
| shared practice: dense minus rerank | 20 | -0.237 | [-0.408, -0.083] | 13,781 | 3.3 | rerank higher |
| shared practice: hybrid minus rerank | 20 | -0.329 | [-0.504, -0.164] | 13,781 | 3.3 | rerank higher |
| own: bm25 minus rerank | 40 | -0.212 | [-0.328, -0.095] | 17,961 | 3.0 | rerank higher |
| own: dense minus rerank | 40 | -0.038 | [-0.151, +0.074] | 17,961 | 3.0 | not distinguishable |
| own: hybrid minus rerank | 40 | -0.118 | [-0.230, -0.013] | 17,961 | 3.0 | rerank higher |

The difference is the cheaper system's score minus the dearer one's, with its paired interval; the savings count Claude calls only, so a system that makes none saves all of the other's.

Systems that do not call Claude, from traces/retrieval/ on the machine that last ran `p2 score` (git ignores that folder, so `p2 check` does not compare this part):

| Trace | System | Queries | Seconds | Milliseconds per query |
| --- | --- | ---: | ---: | ---: |
| traces/retrieval/own-own-ablation-hybrid_dense.jsonl | hybrid_dense | 40 | 1.45 | 36.2 |
| traces/retrieval/own-own-bm25.jsonl | bm25 | 40 | 0.02 | 0.4 |
| traces/retrieval/own-own-dense.jsonl | dense | 40 | 1.12 | 27.9 |
| traces/retrieval/own-own-hybrid.jsonl | hybrid | 40 | 0.95 | 23.7 |
| traces/retrieval/shared-practice-bm25.jsonl | bm25 | 20 | 0.03 | 1.4 |
| traces/retrieval/shared-practice-dense.jsonl | dense | 20 | 0.71 | 35.5 |
| traces/retrieval/shared-practice-hybrid.jsonl | hybrid | 20 | 0.97 | 48.4 |
| traces/retrieval/shared-test-bm25.jsonl | bm25 | 40 | 0.09 | 2.3 |
| traces/retrieval/shared-test-dense.jsonl | dense | 40 | 1.35 | 33.7 |
| traces/retrieval/shared-test-hybrid.jsonl | hybrid | 40 | 1.83 | 45.7 |
<!-- p2:end stretch-cost -->

### The grep agent (option 5)

Your stretch run on some of your own queries against the four systems on the same queries.

<!-- p2:begin stretch-agent -->
_No stretch runs yet (stretch option 5): `uv run p2 run --corpus own --queries eval/own/agent.queries.tsv --system agent --stretch` writes one to runs/own/stretch/, then `uv run p2 score` fills this table._
<!-- p2:end stretch-agent -->

### Your stretch

Write the five things here.

---

## 9. 598E only - repeats and the pre-registered claim

498E students can leave this section as it is; nothing checks it.
598E students replace each line that starts with "598E: write", and `uv run p2 check --final` counts those lines as work still to do until they are gone.

### Repeats on the shared corpus

Three runs of the reranker on the practice queries, and three answers files, with their run-to-run spread and Wilson intervals.

<!-- p2:begin repeats -->
Repeated runs of rerank on shared/practice:

| Run | Recall@10 | MRR@10 | nDCG@10 |
| --- | ---: | ---: | ---: |
| rerank.r1 | 0.758 | 0.800 | 0.765 |
| rerank.r2 | 0.758 | 0.800 | 0.769 |
| rerank.r3 | 0.758 | 0.800 | 0.769 |
| range (max minus min) | 0.000 | 0.000 | 0.004 |

| Comparison | Metric | Mean difference | 95% interval | Reading |
| --- | --- | ---: | ---: | --- |
| rerank.r1 minus hybrid | Recall@10 | +0.167 | [+0.058, +0.292] | rerank.r1 higher |
| rerank.r2 minus hybrid | Recall@10 | +0.167 | [+0.058, +0.292] | rerank.r2 higher |
| rerank.r3 minus hybrid | Recall@10 | +0.167 | [+0.058, +0.292] | rerank.r3 higher |
| rerank.r1 minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | rerank.r1 higher |
| rerank.r2 minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | rerank.r2 higher |
| rerank.r3 minus hybrid | MRR@10 | +0.329 | [+0.164, +0.504] | rerank.r3 higher |
| rerank.r1 minus hybrid | nDCG@10 | +0.321 | [+0.197, +0.448] | rerank.r1 higher |
| rerank.r2 minus hybrid | nDCG@10 | +0.325 | [+0.199, +0.453] | rerank.r2 higher |
| rerank.r3 minus hybrid | nDCG@10 | +0.325 | [+0.199, +0.453] | rerank.r3 higher |

Repeated answers shared/rerank:

| File | Verified (in) | 95% interval | Declined (out) | 95% interval |
| --- | ---: | ---: | ---: | ---: |
| rerank.r1 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| rerank.r2 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| rerank.r3 | 8 of 8 (100%) | [0.676, 1.000] | 4 of 4 (100%) | [0.510, 1.000] |
| range (max minus min) | 0.000 |  | 0.000 |  |

Each repeat answers the same questions, so the repeats are not independent trials and their counts are not pooled into one interval.
<!-- p2:end repeats -->

Does the reranker's gain over its first stage survive the run-to-run variation?
Write what the spread is, how it compares with the gain, and what the Wilson intervals on the verified share and the declined share say about 8 and 4 questions.

598E: write the repeats result here.

### The pre-registered claim

The claim, the smallest effect, the gold-set size and the test are in `PREREG.md`, committed before your own gold-set judgments.
Here, say whether you followed the plan, what the interval turned out to be, and what that means.
The outcome section of `PREREG.md` holds the short version.

598E: write the claim and its outcome here.
