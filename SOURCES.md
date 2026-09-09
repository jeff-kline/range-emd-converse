# Source scope and provenance

This release contains original paper, code, and evidence. It does not contain
third-party PDFs, the archived GEM implementation, private working history,
or retired research programs. The two files in `audit/` are preserved historical
reports: their working-repository paths and commit IDs describe the review
environment, not extra files promised in this release. Audit 02 closes the
ICLR access issue recorded in audit 01. Current release status is in
[ADMISSION.md](ADMISSION.md).

## Closest sources

| Source | Inspected location and relation |
|---|---|
| [Kline 2019](https://doi.org/10.1016/j.dam.2019.02.042) | Published pp.128–141; underlying range-cost geometry and Appendix A's qualified statements |
| [Queyranne–Spieksma–Tardella 1998](https://doi.org/10.1287/moor.23.4.892) | Theorem 3.1(2)–(3), p.899; Theorem 4.1, p.902; classical greedy primal/dual and product-lattice Monge framework |
| [Hirai 2005](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1508.pdf) | Section 2.2, pp.6–7, and pp.25–26; greedy polyhedra and normal-fan machinery |
| [Bryant–Tupper v3](https://arxiv.org/html/2412.07092v3) | Section 2.1 and Theorem 5; coordinate-width diversity and broad support-measure representation |
| [Mehta et al., ICLR 2023](https://openreview.net/forum?id=R98ZfMt-jE) | User-supplied conference-formatted PDF, 23 pages; Theorem 4.3, p.5, and Appendix 7.1, p.15; dual-gradient application, with qualifications recorded in audit 02 |
| [Makur–Singh v2](https://arxiv.org/abs/2309.08475v2) | Proposition 1 and Sections III-C1, III-D; jointly attaining coupling underlying the known branching-star corollary |
| [Barvinok–Lee–Novik](https://arxiv.org/abs/1203.6867) | Theorem 4.1; imported strictly antipodal-set bound |

The review's ten discovery queries, exact mathematical comparisons, and
source-access limitations are in [audit 01](audit/01-independent-review.md).
Neither a general greedy theorem nor a general support representation alone
was identified as stating either exact headline result. The bounded verdict
is SOURCE-NEGATIVE for those statements and PARTIAL-OVERLAP for their known
ingredients. Historical originality remains UNKNOWN.

## Identifiers for nonredistributed sources

The following SHA-256 hashes identify the local research copies actually
examined; they are provenance records, not promises that current download
URLs return identical bytes.

| Source | SHA-256 |
|---|---|
| Published Kline 2019 PDF | `31eab2702bac5411340d74c6d50a5e6d59f6752de0aab226c3463170875baa30` |
| ICLR conference copy | `abf03c6fa5497e9896019c604cf367533be2c6bb622862ed5f02774f241f2798` |
| Hirai PDF | `7c79a3cebc6edaf1d9ae465fbbc9abc19fddf94e2c1e4dbd89e48ddeec085b5e` |
| Bryant–Tupper v3 PDF | `593a72ee1e0d6d0df7f8b2d86539059161b7d1b173b7f464e342945c69949c4b` |
| Makur–Singh v2 PDF | `9acd2177ee7cc9715cf9938c3635879f645de2008a2aff36fb6913ebe592f7e2` |
| Barvinok–Lee–Novik PDF | `5c0df45038aec0b2dd62b285c1054b1bb962c0209055f38f10862c0188391c34` |
| Archived GEM `emd.py`, revision prefix `e0b1021` | `70808b7558bd8c465274310fd9db3af91ead8704c648c98d1cb658377a5212fe` |

QST's author-hosted PDF text was inspected through web extraction; direct
downloads returned HTML, so no verified local PDF hash is asserted. The ICLR
copy was supplied by the author following the canonical link; independent
byte comparison with the challenge-protected remote endpoint was unavailable.
These limits do not mean the technical statements were unread.

The manuscript examined in audit 01 had SHA-256
`75f7f60e713c137124baa8586b33968023993588a0f8204b7ef9e32f25b91b4f`.
The release preserves every theorem, lemma, proposition, corollary and proof
environment from that version. Changes are release metadata, specific
citations, and explanatory review/provenance prose. The release's current
file hashes are in `MANIFEST.sha256`.

Third-party references retain their own rights. The GPL-3.0-only license
applies to this release's original material, not to the cited works.
