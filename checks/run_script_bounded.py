"""60-second wall timeout, one numerical-library thread; observe memory in child."""
import os, subprocess, sys
from pathlib import Path
interpreter, script, output = sys.argv[1:]
env=os.environ.copy()
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    env[key]='1'
r=subprocess.run([interpreter,script],env=env,capture_output=True,text=True,timeout=60)
Path(output).write_text(r.stdout)
Path(output+'.stderr').write_text(r.stderr)
print(r.stdout)
print(r.stderr,file=sys.stderr)
raise SystemExit(r.returncode)
