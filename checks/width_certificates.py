"""Exact quantile/dual certificates and independent raw transport LP checks."""
from fractions import Fraction as F
from itertools import product
import random, json, time, resource, warnings
import numpy as np
from scipy.optimize import linprog
from range_emd import solve as solve_range
warnings.filterwarnings('ignore', message='Unrecognized options detected')
rng=random.Random(202609072)
start=time.monotonic()
records=[]
for case in range(80):
    n=2+case%4; d=1+(case//4)%5
    mass=F(0) if case==0 else F(1+case%3,2)
    X=[]
    for j in range(d):
        w=[rng.randrange(6) for _ in range(n)]
        if not sum(w): w[0]=1
        X.append([mass*F(v,sum(w)) for v in w])
    P=[[sum(x[:k+1]) for k in range(n-1)] for x in X]
    cuts=sorted(set([F(0),mass]+[v for p in P for v in p]))
    coupling={}
    for lo,hi in zip(cuts,cuts[1:]):
        t=(lo+hi)/2
        I=tuple(next((i for i,f in enumerate(p) if t<f),n-1) for p in P)
        coupling[I]=coupling.get(I,F(0))+hi-lo
    assert all(sum(w for I,w in coupling.items() if I[j]==i)==X[j][i] for j in range(d) for i in range(n))
    lo=[min(p[k] for p in P) for k in range(n-1)]
    hi=[max(p[k] for p in P) for k in range(n-1)]
    width=sum(b-a for a,b in zip(lo,hi))
    cost=sum(w*(max(I)-min(I)) for I,w in coupling.items())
    assert width==cost
    q=[]
    for k in range(n-1):
        a=min(range(d),key=lambda j:P[j][k]); b=max(range(d),key=lambda j:P[j][k])
        q.append([int(j==a)-int(j==b) for j in range(d)])
    y=[[sum(q[k][j] for k in range(i)) for i in range(n)] for j in range(d)]
    cells=list(product(range(n),repeat=d))
    assert all(sum(y[j][I[j]] for j in range(d))<=max(I)-min(I) for I in cells)
    assert sum(X[j][i]*y[j][i] for j in range(d) for i in range(n))==width
    max_value=mass*(n-1)-sum(lo)
    assert sum(w*max(I) for I,w in coupling.items())==max_value
    mean_value=sum(F(i,d)*X[j][i] for j in range(d) for i in range(n))
    assert sum(w*F(sum(I),d) for I,w in coupling.items())==mean_value
    rec={'n':n,'d':d,'mass':str(mass),'width':str(width),'primal_cells':len(coupling)}
    if n<=4 and d<=4:
        A=np.array([[int(I[j]==i) for I in cells] for j in range(d) for i in range(n)])
        b=np.array([float(v) for x in X for v in x])
        errors=[]
        for c,expected in [([max(I)-min(I) for I in cells],width),([max(I) for I in cells],max_value),([sum(I)/d for I in cells],mean_value)]:
            r=linprog(c,A_eq=A,b_eq=b,bounds=(0,None),method='highs',options={'threads':1})
            assert r.success, r.message
            err=abs(r.fun-float(expected)); assert err<1e-8
            errors.append(err)
        rec['lp_errors']=errors
    # Compare the reusable replacement against independent certificates and LPs.
    replacement=solve_range(X,with_primal=True)
    assert replacement['value']==width
    assert replacement['primal']==coupling
    assert replacement['dual']==tuple(tuple(v) for v in y)
    records.append(rec)
boundary=solve_range([[1,0],[1,0]],with_primal=True)
assert boundary['value']==0 and boundary['dual']==((0,0),(0,0))
assert solve_range([[1],[1]],with_primal=True)['primal']=={(0,0):F(1)}
print(json.dumps({'reusable_solver_checked':True,'seed' :202609072,'exact_cases':len(records),'lp_solves':3*sum('lp_errors' in x for x in records),
'max_lp_error':max(e for x in records for e in x.get('lp_errors',[])),
'cases':records,'seconds':time.monotonic()-start,'maxrss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2))
