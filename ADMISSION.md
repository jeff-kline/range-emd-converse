# Release assessment

Current verdict: **NOT YET ADMITTED**.
Current state: **TAGGED**, version `0.1.0`, published September 9, 2026.
Frozen commit: `3ce13e87c05d0028b8ecbc8607d8c3f9f834bb77`.
Zenodo archival publication and DOI verification are blocked by the
author-reported HTTP 504 outage. No archive or DOI exists for this release.

Standard: [A Public Standard for This Work, draft 0.4](https://jeff-kline.github.io/posts/research-program/index.html).

| Gate | Status | Disposition |
|---|---|---|
| P1: prior work and credit | PASS | Bounded QST, Hirai, Bryant–Tupper and final ICLR-copy comparisons are recorded. Classical ingredients and known transfers are credited. Exact headline priority remains source-negative within that scope, not proved novel. |
| A1: claims and artifacts | PASS | All 24 statement/proof environments are unchanged from the reviewed source. Separate release consistency review passed; all 13 PDF pages were visually checked and the PDF rebuilt identically. |
| R1: reproduction and stewardship | PARTIAL | All four bounded checks pass. Reproduction code, evidence, license, correction policy and archive route are supplied. The immutable GitHub tag and release are public, and both downloaded assets match their local bytes. DOI archive verification remains pending. |

Passing P1 means the specified comparison was performed and its limits are
visible; it does not assert worldwide originality. Source byte provenance,
including the user-supplied ICLR copy, is in [SOURCES.md](SOURCES.md).
AI review is process evidence, not external expert peer review or a correctness
certificate.

The author authorized release preparation and continuation of work independent
of Zenodo. This includes the accepted Appendix A scope and GPL-3.0-only license.
The clean release excludes private working history, retired research lanes,
and third-party PDFs/code. The release agent owns local edits, checks, and
authorized GitHub publication. The author operates the authenticated archive
portal; the agent can subsequently verify its public record and downloaded
bytes. Email remains prohibited.

## Archive route

Use manual Zenodo upload of the exact `git archive` ZIP of the immutable
version tag. Do not also activate a GitHub-triggered deposit for this version.
Generate the tagged ZIP twice and compare bytes. When Zenodo is restored,
upload that unchanged artifact, then verify title, author, license, version,
record access, version DOI, and downloaded byte identity. Only then update
living metadata to ARCHIVED or ADMITTED. Do not move the public tag.

## Published artifact receipt

[Release v0.1.0](https://github.com/jeff-kline/range-emd-converse/releases/tag/v0.1.0)
contains the reading PDF and exact manual-upload ZIP. Public downloads were
compared byte for byte with the local artifacts.

- ZIP: 337483 bytes; SHA-256 `6a0dd7915864a7b76458721a9d08eaed3cfcbcb25d3771072d738e56006eb832`.
- PDF: 268384 bytes; SHA-256 `8a183a6f5c1b700425f0c89136b751a37021566e67e19bf7352951bd7ba4948c`.

The tagged assessment records the candidate snapshot. This living assessment
records the later publication without changing the immutable tag or ZIP.
