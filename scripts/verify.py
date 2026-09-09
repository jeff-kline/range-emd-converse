"""Run bounded mathematical checks and compare their structural results."""
import argparse
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CHECKS = {
    'width': 'checks/width_certificates.py',
    'dual': 'checks/dual_census.py',
    'classification': 'paper/checks/classification_checks.py',
    'stars': 'paper/checks/star_realization.py',
}
VARIABLE_FIELDS = {'seconds', 'maxrss_bytes_macos', 'max_lp_error', 'lp_errors', 'lp_error'}


def structural(value):
    if isinstance(value, dict):
        return {k: structural(v) for k, v in value.items() if k not in VARIABLE_FIELDS}
    if isinstance(value, list):
        return [structural(v) for v in value]
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', action='store_true')
    args = parser.parse_args()
    env = os.environ.copy()
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
                'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
        env[key] = '1'
    import numpy
    import scipy
    environment = {'python': platform.python_version(), 'platform': platform.platform(),
                   'numpy': numpy.__version__, 'scipy': scipy.__version__}
    print(json.dumps(environment, sort_keys=True), flush=True)
    with tempfile.TemporaryDirectory(prefix='range-emd-checks-') as tmp:
        for name, script in CHECKS.items():
            result = subprocess.run([sys.executable, str(ROOT / script)], cwd=ROOT,
                                    env=env, text=True, capture_output=True, timeout=60)
            if result.returncode:
                raise RuntimeError(f'{script} failed:\n{result.stdout}\n{result.stderr}')
            if result.stderr.strip():
                raise RuntimeError(f'{script} reported stderr:\n{result.stderr}')
            data = json.loads(result.stdout)
            output = Path(tmp) / f'{name}.json'
            output.write_text(json.dumps(data, indent=2) + '\n')
            expected = ROOT / 'evidence' / output.name
            if args.record:
                expected.write_bytes(output.read_bytes())
            elif structural(data) != structural(json.loads(expected.read_text())):
                raise AssertionError(f'{script}: structural evidence differs')
            print(f'PASS {name}', flush=True)
    if args.record:
        (ROOT / 'evidence' / 'environment.json').write_text(json.dumps(environment, indent=2) + '\n')
    print('PASS all four bounded checks', flush=True)


if __name__ == '__main__':
    main()
