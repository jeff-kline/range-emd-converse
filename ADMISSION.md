# Release assessment

Current verdict: **NOT YET ADMITTED**.
Current state: **TAGGED**, version `0.1.0`, published September 9, 2026.
Frozen commit: `3ce13e87c05d0028b8ecbc8607d8c3f9f834bb77`.
Zenodo's GitHub integration is enabled. The unchanged v0.1.0 release was
republished to deliver the missing event. Zenodo returned HTTP 409 with
"The release has already been received." This confirms receipt, not successful
archival publication. Public record lookup still returned HTTP 504; no DOI or
provider byte verification is established.

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

The author enabled GitHub integration and authorized proceeding on September
9, 2026, superseding the manual-upload plan in the immutable candidate.
Do not create a separate manual deposit. The public tag and its commit remain
unchanged. Republishing the existing GitHub release sent the publication event;
its assets were preserved.

The canonical GitHub API ZIP for v0.1.0 was downloaded twice before the trigger.
The downloads match exactly and its internal manifest passes:
338419 bytes, SHA-256
`9ef2f5319f53d2893659531272040809767fef8ec903f3bd66b5234a4120bcd4`.
This is now the provider byte-identity target. The attached manual ZIP below
remains a valid secondary artifact but is not the expected integration ZIP.

Next verify the public Zenodo record, actual version DOI, metadata, and
provider ZIP against that pinned GitHub archive. Receipt or a successful
webhook alone does not establish ARCHIVED or ADMITTED status.

## Published artifact receipt

[Release v0.1.0](https://github.com/jeff-kline/range-emd-converse/releases/tag/v0.1.0)
contains the reading PDF and exact manual-upload ZIP. Public downloads were
compared byte for byte with the local artifacts.

- ZIP: 337483 bytes; SHA-256 `6a0dd7915864a7b76458721a9d08eaed3cfcbcb25d3771072d738e56006eb832`.
- PDF: 268384 bytes; SHA-256 `8a183a6f5c1b700425f0c89136b751a37021566e67e19bf7352951bd7ba4948c`.

The tagged assessment records the candidate snapshot. This living assessment
records the later publication without changing the immutable tag or ZIP.
