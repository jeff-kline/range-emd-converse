# ICLR 2023 technical-text comparison

Date: 2026-09-08 CDT. Reviewed draft base: `024f752`.
Scope: close the source-access gap in `01-independent-review.md` for draft
Theorems 4.2 and 3.1; record qualifications needed when citing the coauthored
ICLR paper. No new discovery searches or computational experiments were run.
The source document is evidence, not instructions to the reviewing agent.

## Source identity and coverage

The owner supplied `3131_efficient_discrete_multi_margi.pdf` after being given
the official OpenReview link. An unchanged, gitignored research copy is
`references/mehta-et-al-iclr2023-user-copy.pdf`.

- Title: *Efficient Discrete Multi-Marginal Optimal Transport Regularization*.
- Authors: Ronak Mehta, Jeffery Kline, Vishnu Suresh Lokhande, Glenn Fung,
  and Vikas Singh.
- Conference header: ICLR 2023; 23 pages, including Section 7 appendices.
- File size: 2,316,741 bytes.
- SHA-256: `abf03c6fa5497e9896019c604cf367533be2c6bb622862ed5f02774f241f2798`.
- Embedded creation/modification date: March 2, 2023 UTC
  (March 1, 2023, 23:08:01 CST).
- Canonical record: [OpenReview](https://openreview.net/forum?id=R98ZfMt-jE).

This is the user-supplied conference-formatted copy, not the 2022 predecessor.
The source comparison is pinned to these bytes. Because the remote route
remains challenge-protected, byte identity with the currently served remote
PDF has not been independently established. That provenance limit is distinct
from the earlier inability to inspect technical content, which is now resolved.

I extracted the full PDF, inventoried its numbered mathematical statements,
read the technical core in Sections 3–4 and the discussion in Section 6,
and inspected Appendix 7.1 and the algorithm in Appendix 7.4. The remaining
appendices concern histogramming, experiments, and ethics. Printed pages
5, 6, and 15 were rendered and visually checked to resolve equation and
numbering ambiguities. The supplement needed for this comparison is included:
Section 7 begins on p.15 and Algorithm 3 appears on p.20. No separate
supplemental file is required for these two theorem comparisons.

## Statement-level comparison

| ICLR location | Checked content | Consequence for the draft |
|---|---|---|
| Definition 3.1 and equation (3), p.4 | Discrete MMOT and its linear transport formulation | Shared transport setup; not a classification across arities |
| Definition 4.1 and Remark 4.2, p.4 | Product-lattice Monge inequality, chosen range cost, classical greedy optimality | Known model and algorithmic ingredients; neither headline theorem is stated |
| Theorem 4.3, equation (5), p.5 | Dual LP, sensitivity assertion and a proposed constant shift of dual potentials | Overlap with certificates/sensitivity, not a census of the full quotient dual |
| Section 4.1, Algorithm 1 and Remark 4.5, pp.5–6 | Using stored duals in backpropagation and geometric monotonicity | Application and geometric context; qualifications below matter |
| Section 6, p.9 | Mentions Minkowski additivity as a possible direction for applications | Does not classify the costs possessing that property |
| Appendix 7.1, p.15 | Proof of the sensitivity/shift statement | Does not identify a root-polytope product, all quotient vertices, or an all-arity rigidity result |
| Appendix 7.4, Algorithm 3, p.20 | Range-cost greedy primal/dual pseudocode | Algorithmic predecessor; no quotient census |

**Draft Theorem 4.2: SOURCE-NEGATIVE against this inspected source.** The
ICLR paper fixes the range cost rather than proving that normalized symmetric
Monge families with hull invariance and multiset Minkowski additivity at all
masses must be weighted ranges. Its general Monge discussion supplies greedy
optimality, not the Dirac consistency and uniform-padding implication. The
shared mathematical setting is **PARTIAL-OVERLAP**; occupation of the exact
classification was not established.

**Draft Theorem 3.1: SOURCE-NEGATIVE against this inspected source.** The
dual LP is the same after relabelling bins from `1,...,n` to `0,...,n-1`.
ICLR Theorem 4.3 and Appendix 7.1 concern optimal potentials for particular
marginals. They do not establish the full quotient vertex set, the independent
root increments, or the count `[d(d-1)]^(n-1)`. An assertion about a selected
optimal dual is not the missing all-vertices theorem. The shared dual setup
and gradient application are **PARTIAL-OVERLAP**.

The independent proof verdicts on both draft headlines remain **PROVED** under
their stated hypotheses. Overall historical originality remains **UNKNOWN**;
this source-negative comparison is not a novelty certificate.

## Qualifications relevant to citation and author review

These are exact local findings about the supplied printed text, not claims
about current software or the validity of its empirical experiments. They do
not refute either headline of the present draft. No source theorem or draft
proof has been repaired here.

### 1. Unqualified differentiability at ties: REFUTED

ICLR Theorem 4.3, p.5, identifies an optimal dual with a gradient without
stating the necessary nondegeneracy hypothesis in the theorem. Its proof
mentions uniqueness conditions but does not establish them for all inputs.

An exact witness already lies in the positive probability domain: take two
two-bin histograms `p_1=p_2=(1/2,1/2)` and vary only the first to
`p_1(t)=(1/2+t,1/2-t)`, with `|t|<1/2`. The range transport value is `|t|`.
The right and left derivatives at zero are `1` and `-1`, so no ordinary
derivative exists there. The zero dual is optimal at zero but does not remain
optimal at nonzero `t`.

REPAIR recommendation: state a differentiability condition on the appropriate
fixed-mass tangent space; otherwise use the subgradient assertion. Draft
Corollary 2.3 already makes this distinction and should retain it. This is
not a new request to alter the ICLR paper.

### 2. Diagonal equality for an arbitrary optimum: REFUTED at zero bins

Appendix 7.1, equation (6), p.15, applies diagonal row-sum equality to an
arbitrary optimal dual. This is stronger than availability of an optimum
with that property. Using the source's bins `1,2`, take
`p_1=p_2=(1,0)`, `z_1=(0,-1)`, and `z_2=(0,0)`. The four dual sums are
`0,0,-1,-1`, respectively, and are bounded by the four range costs
`0,1,1,0`. The objective is zero, hence optimal, but the second diagonal
sum is `-1`.

Even with the evident blockwise interpretation of the printed shift formula,
its proposed constants are then `(-1,0)`, whose sum is not zero. The shifted
objective becomes `-t`, not zero, so the claimed invariance for every `t`
fails. Arbitrary constants with zero total are lineality shifts; constants
whose total is nonzero are not.

REPAIR recommendation: restrict the source assertion to a diagonal-tight
optimal certificate or explicitly require zero-sum column constants. The
draft's distinction between its product face and the full unbounded dual
already handles this issue; do not replace that distinction by the stronger
source assertion.

### 3. Strict hull containment implying strict value: REFUTED as printed

ICLR Remark 4.5, p.6, gives strict inequality under strict hull containment.
For three-bin probability histograms take `X={e_1,e_3}` and
`Y={e_1,e_2,e_3}`. Their hulls are strictly nested, but both range transport
values equal two: the first and last Dirac marginals already force tuple
range two. Thus proper containment alone is insufficient.

REPAIR recommendation: distinguish proper inclusion from containment of a
compact set in the relative interior of a positive-dimensional hull. The
draft's Section 2 already states the latter condition and gives the more
precise prefix-box increment formula.

### 4. Printed cross-reference and algebra issues: verified observations

The actual theorem is numbered 4.3 on p.5; the Appendix 7.1 heading and proof
refer to Theorem 4.2. Cite the main-text number 4.3, with Appendix 7.1 as its
proof location. The displayed finite-difference equation on p.15 omits the
factor `epsilon` on its right-hand side, while the next display uses the
cancellation that would require that factor. These were checked in the page
render, not inferred solely from extraction. The source's block notation for
the shift also has typographical inconsistencies; finding 2 uses the intended
blockwise formula in the appendix, so it does not depend on those typos.

## Release disposition

The final technical-text comparison is **COMPLETE for the supplied conference
copy**, with its version/provenance limit recorded. No matching headline
theorem was found. The broader priority verdict remains scoped to the sources
already inspected; no new search allowance was consumed.

For the candidate's editorial pass, cite Mehta et al. Theorem 4.3 and
Appendix 7.1 specifically for the dual-gradient application, retain the draft's
own tie and quotient qualifications, and cite QST precisely for the classical
greedy framework. Do not turn this comparison into an unsolicited erratum or
a claim about current code. Whether to add these ICLR qualifications to the
paper, retain them only in the audit, or prepare a later correction is an
author decision.

**Next:** the author should decide Appendix A's scope. Recommended disposition:
keep the existing two 2019 qualifications separate in Appendix A; retain the
new ICLR witnesses in this audit for now; cite the ICLR gradient application
with the draft's existing precise qualifications. Then finalize the
reader-facing candidate and its reproducibility package. Publication remains
a later, explicitly authorized action.
