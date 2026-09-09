"""Enumerate raw transport-dual vertices exactly; no root-polytope assumption."""
from fractions import Fraction as F
from itertools import product, combinations
import json, time, resource

def solve(rows, rhs):
    n = len(rows)
    a = [[F(v) for v in row]+[F(b)] for row,b in zip(rows,rhs)]
    for j in range(n):
        p = next((i for i in range(j,n) if a[i][j]),None)
        if p is None: return None
        a[j],a[p] = a[p],a[j]
        q = a[j][j]
        a[j] = [v/q for v in a[j]]
        for i in range(n):
            if i != j and a[i][j]:
                q = a[i][j]
                a[i] = [x-q*y for x,y in zip(a[i],a[j])]
    return tuple(row[-1] for row in a)

def census(n,d):
    # Gauge only d-1 coordinates, preserving the full quotient polyhedron.
    variables = [(j,i) for j in range(d) for i in range(n) if i or j == d-1]
    tuples = list(product(range(n),repeat=d))
    rows = [tuple(int(I[j]==i) for j,i in variables) for I in tuples]
    rhs = [max(I)-min(I) for I in tuples]
    verts = set()
    for active in combinations(range(len(rows)),len(variables)):
        v = solve([rows[i] for i in active],[rhs[i] for i in active])
        if v is not None and all(sum(a*x for a,x in zip(row,v))<=b for row,b in zip(rows,rhs)):
            verts.add(v)
    patterns = set()
    for v in verts:
        z = {var:value for var,value in zip(variables,v)}
        for j in range(d-1): z[j,0] = F(0)
        assert all(sum(z[j,i] for j in range(d)) == 0 for i in range(n))
        pat=[]
        for k in range(n-1):
            q=tuple(z[j,k+1]-z[j,k] for j in range(d))
            assert sorted(q)==[F(-1)]+[F(0)]*(d-2)+[F(1)]
            pat.append((q.index(F(1)),q.index(F(-1))))
        patterns.add(tuple(pat))
    expected=(d*(d-1))**(n-1)
    assert len(verts)==len(patterns)==expected
    return {'n':n,'d':d,'quotient_dimension':len(variables),'raw_constraints':len(rows),
            'vertices':len(verts),'expected':expected,'all_diagonals_tight':True,
            'all_derivatives_roots':True,'canonical_vertices':sorted([[str(x) for x in v] for v in verts])}
start=time.monotonic()
results=[census(2,3),census(3,2),census(2,4)]
print(json.dumps({'checks':results,'seconds':time.monotonic()-start,'maxrss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2))
