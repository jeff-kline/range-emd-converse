# Independent proof review and bounded priority audit

Review date: 2026-09-08 (America/Chicago; 2026-09-09 UTC during source access). Reviewed base: `0a2d0fe` on
`main`. Reviewer: Codex, one reviewing agent. This is a process-separated AI
review of the draft, not external peer review or a certificate of originality.

## Scope, independence, and evidence convention

The owner's handoff authorizes proof review, at most ten literature searches,
and at most five local check runs. No proof or theorem edits, release actions,
remote changes, package installation, paid compute, or email are authorized.
The release skill was inspected for applicability; the owner's explicit
working-repository boundary supersedes its release workflow, which is not
being applied. Historical instructions under `retired/` are not adopted.

Mathematical verdicts below use **PROVED**, **REFUTED** (requiring a witness),
or **UNKNOWN** (with an exact gap when applicable). Priority assessments use
OCCUPIED, PARTIAL-OVERLAP, or SOURCE-NEGATIVE, separately from mathematical
correctness. SOURCE-NEGATIVE never means novel. Statements about checks and
file state are observations, not mathematical proofs.

The cold proof sections below were written before opening `paper/REVIEW.md`,
`paper/CLAIM_MAP.md`, `paper/UNIQUENESS_REVIEW.md`, or `results/`. The handoff
already disclosed the drafting agent's verdicts and named the likely weak
steps; consequently this is not a verdict-blind review. The argument was
reconstructed from `paper/main.tex`. The mandated sanity check was run before
the proof pass; its numerical success was not used as a proof premise.

## 1. Cold pass: Theorem 4.2 and Lemma 4.1

**Verdict: PROVED under the stated all-mass, all-arity hypotheses.** No
counterexample or missing lemma was found. This verdict includes both
directions and uniqueness of the weights.

### Exact reconstruction of N1

Fix one integer `n >= 2` and its ordered bins. For every integer `d >= 1`,
there is a finite nonnegative cost `c_d` on the ordered product of `d` bin
sets, invariant under permutations of the marginal labels. Each cost is
submodular on this product lattice:

`c_d(I meet J) + c_d(I join J) <= c_d(I) + c_d(J)`.

Normalization is the entire unary tensor `c_1(i)=0`. A marginal family is a
nonempty finite multiset of nonnegative histograms, all of some common mass
`m >= 0`. Hull invariance compares any two such families in the same mass
hyperplane, including families of different cardinalities. Addition takes
every pairwise sum, retaining multiplicity: a `d`-family plus an `e`-family
is a `de`-family of mass `m_X+m_Y`. The assumed equation uses precisely these
three arities and allows arbitrary nonnegative common masses. Neither
probability-only addition nor an endpoint-only notion of hull is being used.

### Common quantiles, including zero bins and ties

For positive mass the feasible transport polytope is nonempty and compact.
Minimize the stated cost and then maximize the linear functional with cell
coefficient `(sum_j I_j)^2` on that optimal face. Suppose incomparable cells
`I,J` both have positive mass. Transfer a common positive amount, no greater
than either mass, to their meet and join. In each marginal the two bin labels
are the same multiset before and after, so feasibility is preserved.

Set `a=sum I_j`, `b=sum J_j`, and `t=sum min(I_j,J_j)`. Incomparability gives
both `a-t>0` and `b-t>0`. Submodularity makes the primary objective change
nonpositive, hence zero by optimality. The secondary gain per unit is exactly
`2(a-t)(b-t)>0`, a contradiction. Thus the support is a chain. Parametrizing
its atoms by consecutive intervals of their masses makes every coordinate a
nondecreasing function with its prescribed distribution. Such a function is
the marginal quantile almost everywhere. A zero bin contributes an interval
of length zero; a tied cumulative breakpoint changes only null endpoints.
At mass zero the zero coupling proves the assertion directly. This establishes
Lemma 4.1 without strict positivity or genericity assumptions.

### Dirac reduction does not confuse a hull with its endpoints

For the mass-one family `(e_{I_1},...,e_{I_d})` the only coupling is the unit
atom at `I`, whose value is `c_d(I)`. The convex hull is the simplex face with
vertex set the distinct occurring bin vectors. Repeating or permuting these
vertices preserves that hull. In particular a constant tuple has the unary
cost zero, and every tuple containing both `k` and `k+1`, and no other labels,
has cost `w_k=c_2(k,k+1)`, at every arity where such a tuple exists.

This step alone does NOT identify a tuple containing intermediate bin labels
with a two-endpoint tuple: their Dirac hulls generally differ. The rest of
the proof is what determines those costs, so there is no endpoint-hull
substitution hidden in the argument.

### Padding is authorized, and every transition band is accounted for

For an arbitrary family `X` of common mass `m`, choose `M>m` and the single
histogram `h=(M,...,M)` of mass `nM`. Its unary value is zero. Multiset
addition with this singleton retains arity `d`; the all-mass hypothesis gives
`Phi_c(X+h)=Phi_c(X)`. There is no requirement that `h` have mass `m`, and
no subtraction of histograms is used.

Write `B_{j,k}=(k+1)M+F_{x_j}(k)`. At each cut these breakpoints lie in
`[(k+1)M,(k+1)M+m]`. Successive containing bands have a positive separating
gap `M-m`. For a quantile time in band `k`, all marginals have already
passed their cut `k-1` (if any), and none has passed cut `k+1` (if any).
Thus their indices can only be `k` or `k+1`. Between the least and greatest
`B_{j,k}` both labels occur, except at irrelevant endpoints; this part has
length `max_j F_{x_j}(k)-min_j F_{x_j}(k)` and constant cost `w_k`.
Before the first band, after the last band, in the separating gaps, and in
the nonmixed parts of each band, all indices coincide and the cost is zero.
Coincident breakpoints simply produce a mixed interval of zero length.
These cases partition the entire quantile interval of mass `m+nM`.

Lemma 4.1 therefore computes the padded optimum as the claimed weighted
prefix-width sum. Padding invariance gives the same formula on the original
family. Applying this formula to each mass-one Dirac family now recovers
EVERY tensor entry, since at cut `k` its width is one exactly when
`min I <= k < max I`. The weights do not depend on arity and are nonnegative
by the binary cost assumption; evaluation at `(k,k+1)` proves uniqueness.

### Converse and falsification attempts

For `d>=2`, the cut function on subsets is zero on the empty and full sets
and one on every other set. Its cardinality increments are `1`, then zeros,
then `-1` (for `d=2`, just `1,-1`), hence are nonincreasing. It is
submodular. For `d=1` the cut function is identically zero. Mapping a bin
tuple to `{j:I_j>k}` respects meet and join. Nonnegative sums of these cut
functions satisfy the stated Monge inequality, symmetry, and normalization.
The nested-event quantile proof of Theorem 2.1 applies to each weighted cut.
Widths depend only on the hull and add under the full multiset Minkowski sum.
This proves sufficiency, including zero weights.

The following attempted escape mechanisms fail for explicit reasons:

- An arity- or multiplicity-dependent adjacent cost violates the Dirac hull
  comparison with the two-element family.
- A nonlinear cost of the number of crossed cuts cannot survive padding.
  For example squared range on three bins gives value 4 on `{e_0,e_2}`
  and value 2 after adding `2(1,1,1)`; the latter follows by two disjoint
  mixed bands of unit length and adjacent cost one. It violates additivity
  with a zero-valued singleton.
- Reordering the path can preserve geometric additivity, but for order
  `(0,2,1)` the original-lattice Monge inequality on `(0,2),(1,1)` reads
  `3 <= 1`, which is false.
- Zero weights, zero marginal bins, coincident extrema, `d=1`, and `m=0`
  are covered by the argument rather than excluded exceptions.

## 2. Cold pass: full quotient dual, Theorem 3.1 and Remark 3.2

**Verdict: PROVED**, including completeness, the census, integer
representatives, and the recession decomposition. The bounded face alone
would not suffice; the exposing-objective argument does establish that all
quotient vertices belong to it.

Let `a_I` be the tuple normal with one entry 1 in every marginal column.
A direction annihilates all tuple normals iff varying one tuple coordinate
shows it is constant in that column, with the column constants summing to
zero. This is exactly `L`. The dual has an interior point (take all entries
strictly negative), so the quotient is full dimensional in
`E=L^perp`, of dimension `nd-d+1`. Equivalently `E` consists of arrays with
equal column sums. The quotient has no lineality.

### Product face and integer representatives

Every diagonal inequality has right side zero. Their summed slack vanishes
iff every diagonal is tight, defining a nonempty face `P`. On that face
`sum_j z_j(0)=0`, so subtracting the individual values `z_j(0)` is an allowed
and unique gauge in which all of them vanish. The differences
`q_k(j)=z_j(k+1)-z_j(k)` sum to zero at each cut. The two-bin tuple
inequalities are exactly `sum_{j in S}q_k(j)<=1` for nonempty proper `S`.
For a zero-sum vector this is equivalent to total positive part at most one.
Transport its positive part to its negative part to express it as a
nonnegative sum of roots `e_a-e_b` with coefficient sum at most one.
Since zero is in the convex hull of opposite roots, this is precisely `R_d`.

Conversely any independent choices from these root polytopes satisfy every
tuple inequality: outside the interval from the tuple's minimum to maximum,
the relevant subset is empty or full and contributes zero; at each other
cut it contributes at most one. Thus the local inequalities lose no distant
tuple constraints. Each root is exposed by a vector with the indicated
unique highest and lowest coordinates. The root polytope has exactly
`d(d-1)` vertices, and the product has their independent sequences. Partial
sums of the root increments give integer potential entries in the stated
gauge, establishing the claimed integral representatives.

### Completeness: an admissible objective exposing ANY quotient vertex

At a quotient vertex `v`, the active normals span `E`: otherwise a nonzero
direction in `E` orthogonal to all of them admits sufficiently small moves
of either sign preserving all inequalities (there are finitely many inactive
constraints and their slacks are positive), contradicting extremality.

Sum ALL its active tuple normals to obtain `x`. Every column sum is the
number of active tuples, hence equal and positive. Every individual entry
is positive as well. Indeed if entry `(j,i)` vanished, nonnegativity of the
normals would force that entry to vanish on their whole span. The coordinate
functional is nonzero on `E` (the all-ones array lies in `E`), contradicting
the span. So `x` is a valid strictly positive family, not an arbitrary
objective that might be outside the transport domain.

For any feasible `z`, `x.z` is bounded by the sum of the active right-hand
sides, attained at `v`. Equality forces equality term by term, because each
slack is nonnegative and each coefficient in the sum is positive. Spanning
then forces `z-v` to lie in `L`. Thus this objective uniquely exposes `v`
modulo lineality, even though the quotient is unbounded.

The prefix-width primal certificate and Proposition 2.2 supply for this
same `x` an optimum whose diagonal sums are all zero. Uniqueness identifies
it with `v` in the quotient. Every quotient vertex is therefore on `P/L`.
Conversely a vertex of that face is a vertex of the quotient. This closes
the completeness step and proves the full count `[d(d-1)]^(n-1)`.

Strictly positive marginals do not by themselves guarantee a unique
optimizer; uniqueness here comes from the sum of spanning active normals.
That distinction is respected in the proof. Ties in the prefix certificate
do not invalidate this reasoning: if a choice produced a different quotient
optimum it would contradict the already established unique exposure.

### Recession directions and decomposition

Homogenizing the inequalities gives `sum_j r_j(I_j)<=0` for all tuples.
Maximizing independently in each column yields exactly
`sum_j max_i r_j(i)<=0`. Choose constants at least these maxima and allocate
the nonnegative deficit to one column to make their sum zero. Subtracting
them leaves a nonpositive array, proving
`rec D = -R_+^(nd)+L`; the reverse inclusion is immediate.
The pointed quotient is a polyhedron, so its vertex--recession
decomposition applies. Its vertex hull is `P/L`, giving
`D=P+rec D` after lifting. In particular the quotient itself is unbounded;
it is not being identified with the bounded product.

## 3. Cold pass: requested auxiliary statements

**Theorem 2.1: PROVED.** At cut `k` the cost event has measure
`mu(union_j A_j)-mu(intersection_j A_j)`, at least the largest prefix mass
minus the smallest. Common quantiles nest these events and simultaneously
attain every lower bound. Null endpoints and mass zero cause no exception.
This proof also validates the explicit dual used in the census.

**Theorem 5.3 and Theorem 5.4: PROVED under the stated non-induced,
no-isolate convention.** Restricting prefix functionals to an affine hull
produces strict antipodal witnesses. Conversely finitely many witnessing
linear functionals can be scaled and added to the uniform increasing prefix
sequence; sufficiently small positive scale ensures all bins are positive.
The resulting affine dimension is at most the source dimension. These two
inequalities prove equality of the minimum dimensions; the map need not
preserve the dimension of every nonminimal source realization.

For the star, `p_0=(0,1)`, `p_i=(t_i,t_i^2)` and
`ell_j(x,y)=y-2t_j x` give
`ell_j(p_i)-ell_j(p_j)=(t_i-t_j)^2>0` for `i != j`.
Every leaf value is between `-1/16` and `3/16`, whereas the apex value is
one. Thus each requested leaf is the unique minimum and the apex the
unique maximum. The specified scale `1/(4n)` keeps successive prefixes
strictly separated: the worst change in witness values is at most `17/16`,
less than four, with the boundary bins positive as well. A one-dimensional
finite set has only two uniquely exposed labels; because every label is
incident to an edge, a star with at least two leaves cannot live in dimension
one. A single edge is realized by a segment and cannot live in dimension
zero. Extra strict antipodal pairs are allowed. No originality conclusion
about this construction follows from this correctness verdict.

## 4. Comparison with internal reviews

After recording Sections 1–3, I read `paper/REVIEW.md`, `paper/CLAIM_MAP.md`,
`paper/UNIQUENESS_REVIEW.md`, and `results/04-dual-vertices.md` and
`results/03-additive-costs.md`. Their arguments agree with the cold conclusions.
No new mathematical premise from those files was needed to sustain either
headline verdict. My proofs share the draft's mechanisms: uncrossing, Dirac
repetition, separated padding, and active-normal exposure. This is an
independent check of those mechanisms, not a claim of a different proof.

The uniqueness review's shorter Dirac-only padding route was first encountered
in that post-pass read and is not counted as an independently discovered route.
The historical results and source ledgers supplied the Hirai source pointer
and access history for the priority pass. I did not rerun or independently
certify their full-dual enumeration, archived GEM reproduction, or branching
formula experiments. The report does not inherit their verdicts on unaudited
claims. In particular Appendix A placement and the final ICLR text remain
outside any positive verdict below.

## 5. Bounded priority audit

### Exact source comparisons

**QST 1998: PARTIAL-OVERLAP with both headlines; the greedy ingredient is
OCCUPIED.** The author-hosted journal PDF was readable through web extraction
(17 pages), despite a direct download returning HTML. Theorem 3.1(2), p.899,
characterizes costs for which their greedy primal algorithm is optimal for
all feasible demands; part (3) supplies a basic optimal dual. Theorem 4.1,
p.902, relates product submodularity to its two-dimensional restrictions.
The discussion on p.901 also gives the TDI consequence. These identify the
classical basis of Lemma 4.1 and dual integrality. They do not state the
all-arity hull/padding classification or the range-specific product and count
in the inspected passages. QST's extra zero symbols are auxiliary; the
transport specialization in Section 2 uses the nonzero chain entries, which
must be relabelled to our bins rather than mistaken for a gauge fixing.
Reference: [QST journal text](https://feb.kuleuven.be/public/u0037710/papers/mor1998paper.pdf),
[journal DOI](https://doi.org/10.1287/moor.23.4.892).

**Hirai, RIMS1508 (2005): PARTIAL-OVERLAP with the dual mechanism.** I read
the existing local PDF's Section 2.2, especially Theorem 2.5, Corollary 2.7,
Proposition 2.8 and Corollary 2.10, pp.6–7, and the product/distributive-lattice
discussion around Theorem 3.36 and Proposition 3.37, pp.25–26. These connect
greedy optimization, coarsening of normal fans, and integral systems. The
specific identification of coincident greedy outputs with independent root
choices at cuts is not supplied by these statements. In particular a general
normal-fan theorem does not, without that specialization, evaluate our vertex
count. Reference: [Hirai preprint](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1508.pdf).
No claim is made about every earlier source cited there. The additional
Tsukuba PDF `885.pdf` surfaced in search but yielded no machine-readable text;
it is not counted as negative evidence.

**Bryant–Tupper v3: PARTIAL-OVERLAP with Theorem 4.2's geometry.** Section
2.1 identifies coordinate range sums as l1 diversity; Theorem 5 represents
linear semidiversities by positive spherical measures with zero first moment.
This gives the broad geometric envelope, not a restriction to prefix
directions. Reference: [version 3, Theorem 5](https://arxiv.org/html/2412.07092v3).
The comparison is substantive: under the prefix map the draft's functional
uses masses `w_k` at each of the two signed coordinate unit vectors. The
mean-width example of Section 2.1 instead allows all directions. As checked
in the manuscript, adjacent Dirac pair values one and endpoint value
`sqrt(2)` violate the original-order Monge inequality `2 <= sqrt(2)`.
Thus the general support representation does not by itself imply the
fixed-order transport classification. This last obstruction is a direct
mathematical deduction, not a theorem attributed to that source.

**Final Mehta et al. ICLR 2023 technical comparison: UNKNOWN.** The
[official paper endpoint](https://openreview.net/pdf?id=R98ZfMt-jE) returned
a browser challenge through both web and direct download. A search-discovered
hashed OpenReview PDF endpoint also returned HTML. The public PDF API returned
HTTP-status information `403`, `ChallengeRequiredError`. The
[author's publication page](https://ronakrm.github.io/research/) and
[author repository](https://github.com/ronakrm/demd) link back to OpenReview;
they did not supply a final technical copy. The search index exposes the
conference title page, but that is not an inspection of the final theorems.
No overlap, omission, correction, or absence verdict about the final technical
text is issued. Neither the abstract nor the 2022 predecessor fills this gap.

### Scope and interpretation of the priority verdicts

For each EXACT headline statement the bounded result is **SOURCE-NEGATIVE
in the inspected scope**, with the source-level partial overlaps above.
The historical originality of each theorem is **UNKNOWN**. The scope consists
of the cited QST statements and transport setup, Hirai passages, Bryant–Tupper
v3 representation and examples, plus the ten discovery queries below.
It explicitly excludes the inaccessible final ICLR technical text and unread
sources cited by the inspected papers. A general greedy algorithm can imply
many special-case results after work; failure to find an explicit count is
not a proof that the count deserves a novelty claim. No source was shown to
occupy Theorem 4.2, so the owner's prior-art stop trigger was not activated.

### Ten-query ledger

The entire new search allowance was used; opens, in-page finds and document
extraction were source access, not additional search queries. Queries 1–2
found useful greedy sources; 3 and 6 pursued the final ICLR text; 5 supplied
no stronger classification source; 4 and 7–9 were largely unproductive;
10 supplied the alternative hashed OpenReview link but not readable text.
Irrelevant results, including Monge–Ampere material, were not mathematical
evidence.

1. `Queyranne Spieksma Tardella 1998 general class greedily solvable linear programs pdf`
2. `submodular product lattice polyhedron vertices greedy multi index transportation Monge dual`
3. `"Efficient Discrete Multi Marginal Optimal Transport Regularization" pdf`
4. `"Monge" cost characterization "translation" invariant -Ampere -Ampère`
5. `"Minkowski additive" "diversities" transport`
6. `"Efficient Discrete" "pdf" site:cs.wisc.edu`
7. `"Monge" "hull invariant"`
8. `"range cost" "dual" "vertices"`
9. `"Monge" "Minkowski additive" classification`
10. `"R98ZfMt-jE" "pdf" Mehta`

## 6. Verification and disposition

Observed sanity results: initially clean tree, the two expected commits,
all four `SOURCE_MANIFEST.sha256` entries verified, and a successful
two-pass 13-page LaTeX build. The build changed the tracked PDF bytes; the
pre-review PDF was restored directly from `HEAD`, preserving the manuscript.
One local numerical check run used the prescribed venv for both the bounded
runner and `paper/checks/classification_checks.py`. It returned 122 LP solves,
11,467 Monge comparisons, and maximum LP error `1.1657341758564144e-15`.
These observations support reproducibility only. The existing staging
manifest was not regenerated. No source PDFs are to be committed.

Budget used: **10/10 discovery searches; 1/5 mathematical check runs**, plus
the mandated paper build and file/hash checks. No additional numerical tests
were needed. The sole check reused the author's script; it is reproduction,
not newly authored independent numerical evidence.

Reviewed manuscript SHA-256:
`75f7f60e713c137124baa8586b33968023993588a0f8204b7ef9e32f25b91b4f`.
The local Hirai PDF SHA-256 is
`7c79a3cebc6edaf1d9ae465fbbc9abc19fddf94e2c1e4dbd89e48ddeec085b5e`.
QST was inspected through the public web extraction, not a locally verified
PDF; there is no new QST file hash to certify. Temporary failed retrievals
were identified as HTML/JSON, not retained as purported source PDFs.

| Theorem | Mathematical verdict | Priority disposition |
|---|---|---|
| 4.2, normalized classification | **PROVED** under N1, including cost recovery and converse | **SOURCE-NEGATIVE**, bounded scope above; originality **UNKNOWN** |
| 3.1, full quotient census | **PROVED**, including completeness and integer representatives | **SOURCE-NEGATIVE**, bounded scope above; originality **UNKNOWN** |
| 2.1, prefix widths | **PROVED** | Classical ingredient; no new priority claim |
| 4.1, common-quantile lemma | **PROVED** at zeros and ties | **OCCUPIED** greedy ingredient: QST 3.1(2) |
| 5.3, dimension reduction | **PROVED** with the stated conventions | Originality **UNKNOWN**, not searched in this two-headline audit |
| 5.4, star dimensions | **PROVED** | Originality **UNKNOWN**, not searched in this two-headline audit |

### Ranked repair list for the referee/author

1. **Priority evidence repair:** obtain and inspect an authenticated final
   ICLR 2023 technical copy and supplement. Until then the required final-text
   comparison is UNKNOWN and the priority gate remains incomplete. No theorem
   repair is indicated by this access failure.
2. **Attribution repair:** in the author's next revision, anchor the classical
   greedy claim to QST 3.1(2)–(3), distinguish general integrality/greedy
   machinery from the specialized product/count, and retain the scoped
   contribution wording. This report updates the source ledgers only; it
   does not rewrite the paper or claim that the existing attribution is false.
3. **Author disposition:** review Appendix A's placement and any historical
   correction separately. This audit does not authorize a GEM repair or
   establish any defect in an uninspected current implementation. The remaining
   provenance and submission decisions in `RELEASE_DESTINATION.md` are still
   future work.

**Proof repairs required for Theorems 4.2 and 3.1: none identified.**
No headline counterexample was found and no source was proved to occupy 4.2;
therefore no fatal-result escalation was triggered. The source-access limit
above is the explicit unresolved item. This report supplies the requested
process-separated proof assessment; it does not declare release admission or
completion of all five destination gates.

**ONE NEXT TASK (not started):** obtain a verified final ICLR 2023 paper and
supplement, then make a theorem-by-theorem comparison with draft Theorems 4.2
and 3.1 in a separate local audit. Require the exact source version and page/
theorem locations; use no new broad-search campaign or release actions.
