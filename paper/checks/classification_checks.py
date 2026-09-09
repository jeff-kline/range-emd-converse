"""Frozen N1 checks: independent raw LPs, padding, and failed-axiom controls."""
from fractions import Fraction as F
from itertools import product
import json, random, resource, time, warnings
import numpy as np
from scipy.optimize import linprog
warnings.filterwarnings('ignore',message='Unrecognized options detected')
start=time.monotonic();rng=random.Random(202609073)
counts={'lp_solves':0,'monge_pairs':0};maxerr=0.

def prefixes(X): return [[sum(x[:k+1]) for k in range(len(x)-1)] for x in X]
def widths(X):
    P=prefixes(X)
    return [max(p[k] for p in P)-min(p[k] for p in P) for k in range(len(P[0]))]
def quantile(X,c):
    P=prefixes(X);m=sum(X[0]);cuts=sorted({F(0),m}.union(t for p in P for t in p));value=F(0)
    for a,b in zip(cuts,cuts[1:]):
        t=(a+b)/2; I=tuple(next((k for k,f in enumerate(p) if t<f),len(p)) for p in P)
        value+=(b-a)*c(I)
    return value

def lp(X,c,expected):
    global maxerr
    n=len(X[0]);d=len(X);cells=list(product(range(n),repeat=d))
    A=np.array([[int(I[j]==k) for I in cells] for j in range(d) for k in range(n)])
    r=linprog([float(c(I)) for I in cells],A_eq=A,b_eq=[float(v) for x in X for v in x],bounds=(0,None),method='highs',options={'threads':1})
    assert r.success,r.message
    err=abs(r.fun-float(expected));maxerr=max(maxerr,err);assert err<1e-8
    counts['lp_solves']+=1
    return r.fun

def sample(m):
    a=[rng.randrange(1,8) for _ in range(3)];return [m*F(v,sum(a)) for v in a]
records=[]
for case in range(24):
    X=[sample(F(1,2)),sample(F(1,2))];Y=[sample(F(3,2)),sample(F(3,2))]
    w=[F(rng.randrange(4)) for _ in range(2)]
    def c(I): return sum(w[k] for k in range(min(I),max(I)))
    S=[[a+b for a,b in zip(x,y)] for x in X for y in Y]
    vals=[sum(a*b for a,b in zip(w,widths(Z))) for Z in (X,Y,S)]
    assert vals[2]==vals[0]+vals[1]
    for Z,v in zip((X,Y,S),vals):lp(Z,c,v)
    hull=X+[[F(1,3)*a+F(2,3)*b for a,b in zip(*X)]]
    lp(hull,c,vals[0])
    M=F(2);padded=[[v+M for v in x] for x in X]
    assert quantile(padded,c)==vals[0];lp(padded,c,vals[0])
    records.append({'weights':list(map(str,w)),'X':[[str(v) for v in x] for x in X],
                    'Y':[[str(v) for v in y] for y in Y],'values':list(map(str,vals))})
# Squared range is Monge, but common padding changes its value.
for n,d in ((3,2),(3,3),(3,4),(4,3)):
    cells=list(product(range(n),repeat=d));c=lambda I:(max(I)-min(I))**2
    for I in cells:
        for J in cells:
            meet=tuple(min(a,b) for a,b in zip(I,J));join=tuple(max(a,b) for a,b in zip(I,J))
            assert c(meet)+c(join)<=c(I)+c(J)
            counts['monge_pairs']+=1
X=[[F(1),F(0),F(0)],[F(0),F(0),F(1)]]
padded=[[v+2 for v in x] for x in X];c=lambda I:(max(I)-min(I))**2
assert quantile(X,c)==4 and quantile(padded,c)==2
lp(X,c,4);lp(padded,c,2)
# Non-Monge, reordered path retains the other functional invariances.
ranks=(0,2,1);c=lambda I:max(ranks[i] for i in I)-min(ranks[i] for i in I)
I=(0,2);J=(1,1);meet=(0,1);join=(1,2)
assert c(meet)+c(join)==3>c(I)+c(J)==1
print(json.dumps({'seed':202609073,**counts,'weighted_instances':records,'max_lp_error':maxerr,
'squared_range_padding':{'before':4,'after':2},'permuted_path_monge_violation':{'lhs':3,'rhs':1},
'seconds':time.monotonic()-start,'maxrss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2))
