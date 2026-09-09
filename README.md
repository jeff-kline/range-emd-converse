# Prefix-width rigidity and dual geometry of multi-marginal earth moving

Jeffery Kline · Version 0.1.0 · September 8, 2026

[Read the paper](paper/main.pdf) · [TeX source](paper/main.tex) ·
[Verification](REPRODUCIBILITY.md) · [Citation](CITATION.cff)

Several histograms on a line can be matched at once by charging each unit of
matched mass the distance between its leftmost and rightmost bins. The minimum
cost is the sum, over cuts between adjacent bins, of the largest cumulative
mass minus the smallest. This gives exact optimal couplings and dual certificates.

The main result is a converse. For symmetric, finite, nonnegative Monge cost
families with zero unary cost, hull invariance and Minkowski additivity hold
at every common mass and every arity if and only if the costs are nonnegative
weighted ranges. The bin order is fixed, hull comparisons permit different
arities, and Minkowski addition retains every pairwise sum with multiplicity.
Unit cost at every adjacent pair recovers ordinary range-cost EMD.

The paper also counts every vertex of the full transport dual after quotienting
out lineality. For `n,d >= 2`, there are exactly `[d(d-1)]^(n-1)` vertices,
with integer representatives. The quotient is unbounded; a product of root
polytopes is its vertex-containing face. Star endpoint patterns with at least
two leaves have minimum affine dimension two.

## Context and evidence

Common-quantile optimality and the general greedy primal/dual framework are
classical. Kline (2019) established the underlying geometric properties;
Mehta et al. (ICLR 2023) used dual solutions for gradients. The paper separates
those ingredients from the classification and full-dual census. The branching
star formula is a known corollary of Makur–Singh. Neither the strict-antipodality
example nor the imported complete-graph bounds are claimed as new.

The headline proofs survived a separate AI review. Exact rational checks and
raw linear programs test representative cases; they do not prove the general
statements. The bounded source comparison did not identify either exact
headline theorem in the inspected literature. Historical originality remains
unestablished. This work has not undergone external expert peer review.

- [Proof review](audit/01-independent-review.md)
- [Final ICLR technical comparison](audit/02-iclr-final-comparison.md)
- [Source scope and provenance](SOURCES.md)
- [Release assessment](ADMISSION.md)

## Use and reproduce

Build with `make paper`. The exact solver is `checks/range_emd.py` and needs
only Python's standard library. The verification suite additionally uses
NumPy and SciPy in a virtual environment:

```sh
make verify PYTHON=/path/to/venv/bin/python
```

Replace the interpreter path with your environment; see
[REPRODUCIBILITY.md](REPRODUCIBILITY.md) for tested versions, expected counts,
and the distinction between exact checks and floating-point LP solves.

## Version, license, and stewardship

This is the version 0.1.0 preprint and reproducibility bundle. The public repository is [range-emd-converse](https://github.com/jeff-kline/range-emd-converse).
[GitHub release v0.1.0](https://github.com/jeff-kline/range-emd-converse/releases/tag/v0.1.0)
was published September 9, 2026. Permanent archiving and a DOI are pending: the author reports that Zenodo
returns HTTP 504. The author has enabled GitHub integration, and Zenodo confirms receipt of
the release. Public record and downloaded-archive verification remain pending;
no DOI is yet verified. Do not create a duplicate manual deposit.
See [ADMISSION.md](ADMISSION.md) for the current state.

Copyright (C) 2026 Jeffery Kline. The original paper, TeX, prose, code, and
evidence are licensed under **GPL-3.0-only**; see [LICENSE](LICENSE).
Third-party reference PDFs and third-party source code are excluded.
The [correction policy](CORRECTIONS.md) preserves prior public versions.

AI assisted the mathematical development, proof examination, code, literature
comparison, and prose under the author's direction. The author takes
responsibility for the work and its correction. AI agreement is not peer review.
