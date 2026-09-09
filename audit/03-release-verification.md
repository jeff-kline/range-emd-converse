# Release verification, v0.1.0

Prepared September 8, 2026. This is an AI-assisted release audit, not external
expert peer review or a certificate of originality.

- All 24 theorem, lemma, proposition, corollary and proof environments match
  the reviewed working source at commit `c13f915` exactly. Changes concern
  release prose, precise citation pointers, version metadata and deterministic
  PDF output. Appendix A retains the two previously reviewed qualifications.
- The 13-page PDF built with two pdfLaTeX passes, with no reported LaTeX
  warnings or overfull/underfull boxes. All pages were rendered and visually
  inspected. A second build produced identical bytes. PDF SHA-256:
  `8a183a6f5c1b700425f0c89136b751a37021566e67e19bf7352951bd7ba4948c`.
- The width, dual, classification and star checks passed within the individual
  60-second bounds. Their JSON evidence and environment versions are included.
  Numerical LP checks support the symbolic proofs; they do not replace them.
- A separate read-only agent checked claims, scope, author/title/version,
  GPL-3.0-only licensing, citations, local links, reproduction instructions,
  Appendix A disposition and no-DOI status. Verdict: PASS, no must-fix findings.
  Its minor bytecode observation was resolved by disabling bytecode writes in
  verification subprocesses.
- The clean package excludes working git history, retired research branches,
  third-party reference PDFs and third-party code. The source comparisons are
  preserved as historical audits with their limits explained in SOURCES.md.
- The author authorized public release. Zenodo remains blocked by the reported
  HTTP 504 outage. No DOI or completed archival admission is claimed. The
  immutable GitHub version and exact tagged ZIP are the next publication steps;
  provider upload and downloaded-byte verification remain for archival release.
