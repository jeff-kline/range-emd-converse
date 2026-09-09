# Reproduction

The paper proves the all-parameter claims. The finite checks below validate
identities, boundary cases, and representative raw LP instances. They do not
establish originality or replace the proofs.

## Environment

Use Python in a virtual environment with the versions in `requirements.txt`:
NumPy 2.0.2 and SciPy 1.13.1. The exact solver and quotient-dual enumeration
use only the standard library. The numerical tests require NumPy/SciPy.
No dependency installation is needed if those libraries already exist in an
environment. The verification script records the actual interpreter, platform,
and library versions without recording private filesystem paths.

Build dependencies: `make`, `pdflatex`, the standard packages declared in
`paper/main.tex`, and optionally Poppler (`pdfinfo`, `pdftoppm`) for visual
inspection. The supplied PDF was built with pdfTeX 1.40.22 (TeX Live 2021).
Creation timestamps and PDF trailer IDs are omitted for repeatable builds
with the same TeX toolchain. Different TeX versions can produce different
bytes without changing the mathematical text.

## Commands

From the repository root:

```sh
make paper
make verify PYTHON=/path/to/venv/bin/python
shasum -a 256 -c MANIFEST.sha256
```

The interpreter path is an example to replace. On GNU/Linux, `sha256sum -c
MANIFEST.sha256` is equivalent. The verification harness uses its own Python
interpreter for each child, limits each to 60 seconds, and sets numerical
thread counts to one. Temporary output is removed automatically. A timeout
on a slower machine is a check failure to investigate, not a mathematical
counterexample.

## Expected checks

| Check | Expected evidence |
|---|---|
| `checks/width_certificates.py` | 80 exact rational cases, 144 raw LP solves; quantile marginals, cost, dual inequalities and reusable solver agree |
| `checks/dual_census.py` | Complete rational enumeration of the full quotient: 6, 4, 12 vertices for `(n,d)=(2,3),(3,2),(2,4)` |
| `paper/checks/classification_checks.py` | 24 weighted instances, 122 LP solves, 11,467 Monge comparisons; padding and failed-axiom controls |
| `paper/checks/star_realization.py` | Seven star sizes: 2, 3, 4, 7, 11, 20, 32 leaves; exact positivity, endpoints and affine rank, plus two raw LP solves |

The original scripts assert exact equality for rational quantities and an
absolute tolerance of `1e-8` for LP comparisons. The harness also compares
structural results with the recorded JSON evidence. Time, memory, and small
LP residuals may vary and are excluded from bytewise result comparisons.
Each child assertion must still pass.

The field `maxrss_bytes_macos` is the original script's macOS memory reporting;
on Linux `ru_maxrss` uses different units. Treat it as machine-specific
performance information, not mathematical evidence. Recorded results were
generated on macOS. The reusable solver returns exact rational values; pass
integers or `fractions.Fraction` to avoid introducing binary float values.

Appendix A's historical GEM reproduction is a prior observation tied to the
source hash in [SOURCES.md](SOURCES.md). The third-party implementation is not
bundled or executed by this suite. Its explicit two-bin dual violation and
the transverse-translation witness can be checked directly from the paper.

## Recorded evidence and integrity

The files in `evidence/` contain this candidate's four successful outputs and
environment record. `scripts/verify.py --record` regenerates those outputs
and is a maintainer operation that invalidates the manifest until it is
regenerated. Normal `make verify` does not change the repository.
