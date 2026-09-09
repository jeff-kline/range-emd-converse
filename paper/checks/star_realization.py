"""Exact rational star endpoint construction and small raw transport LPs."""
from fractions import Fraction as F
from itertools import product
import json, resource, time, warnings
import numpy as np
from scipy.optimize import linprog
warnings.filterwarnings('ignore',message='Unrecognized options detected')
start=time.monotonic();records=[]
for s in (2,3,4,7,11,20,32):
    n=s+1;eps=F(1,4*n);ts=[-F(1,4)+F(j,2*(s-1)) for j in range(s)]
    points=[(F(0),F(1))]+[(t,t*t) for t in ts]
    P=[[F(k+1,n)+eps*(y-2*ts[k]*x) for k in range(s)] for x,y in points]
    X=[[p[0]]+[p[k]-p[k-1] for k in range(1,s)]+[1-p[-1]] for p in P]
    assert all(v>0 for x in X for v in x)
    assert all(sum(x)==1 for x in X)
    for k in range(s):
        values=[p[k] for p in P]
        assert values.index(min(values))==k+1 and values.count(min(values))==1
        assert values.index(max(values))==0 and values.count(max(values))==1
    # Exact affine rank: two independent differences and every row in their span.
    A=[v-u for u,v in zip(P[0],P[1])];B=[v-u for u,v in zip(P[0],P[2])]
    det=A[0]*B[1]-A[1]*B[0];assert det
    for p in P:
        V=[v-u for u,v in zip(P[0],p)]
        a=(V[0]*B[1]-V[1]*B[0])/det;b=(A[0]*V[1]-A[1]*V[0])/det
        assert all(v==a*x+b*y for v,x,y in zip(V,A,B))
    value=sum(max(p[k] for p in P)-min(p[k] for p in P) for k in range(s))
    rec={'leaves':s,'bins':n,'labels':len(X),'affine_dimension':2,'minimum_bin':str(min(v for x in X for v in x)),
         'value':str(value),'rational_parameters':list(map(str,ts))}
    if s<=3:
        cells=list(product(range(n),repeat=n));Aeq=np.array([[int(I[j]==i) for I in cells] for j in range(n) for i in range(n)])
        r=linprog([max(I)-min(I) for I in cells],A_eq=Aeq,b_eq=[float(v) for x in X for v in x],bounds=(0,None),method='highs',options={'threads':1})
        assert r.success and abs(r.fun-float(value))<1e-8
        rec['lp_error']=abs(r.fun-float(value))
    records.append(rec)
print(json.dumps({'cases':records,'lp_solves':2,'seconds':time.monotonic()-start,
'maxrss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2))
