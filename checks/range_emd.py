"""Exact range-cost EMD via prefix widths, with feasible dual and optional primal.

Local research implementation. Standard library only. Inputs are equal-mass,
nonnegative histograms; use ints/Fractions for intentional exact rational data.
The value/dual pass uses O(nd) arithmetic operations. Producing a primal coupling
is optional and has additional breakpoint-merging/output cost.
"""
from bisect import bisect_right
from fractions import Fraction


def solve(histograms, *, with_primal=False):
    X=tuple(tuple(Fraction(v) for v in x) for x in histograms)
    if not X: raise ValueError('At least one histogram is required')
    n=len(X[0]); d=len(X)
    if n==0 or any(len(x)!=n for x in X): raise ValueError('Use equally sized nonempty histograms')
    if any(v<0 for x in X for v in x): raise ValueError('Negative mass')
    mass=sum(X[0])
    if any(sum(x)!=mass for x in X): raise ValueError('Unequal total masses')
    prefixes=[]
    for x in X:
        p=[]; acc=Fraction(0)
        for v in x[:-1]:
            acc+=v; p.append(acc)
        prefixes.append(p)
    intervals=[]; dual=[[0]*n for _ in X]; witnesses=set()
    for k in range(n-1):
        a=min(range(d),key=lambda j:prefixes[j][k])
        b=max(range(d),key=lambda j:prefixes[j][k])
        intervals.append((prefixes[a][k],prefixes[b][k]))
        witnesses.update((a,b))
        for j in range(d):
            dual[j][k+1]=dual[j][k]+int(j==a)-int(j==b)
    result={'value':sum((b-a for a,b in intervals),Fraction(0)),
            'dual':tuple(tuple(y) for y in dual),'prefix_intervals':tuple(intervals),
            'witness_indices':tuple(sorted(witnesses))}
    if with_primal:
        breaks=sorted({Fraction(0),mass}.union(v for p in prefixes for v in p))
        coupling={}
        for lo,hi in zip(breaks,breaks[1:]):
            t=(lo+hi)/2
            I=tuple(bisect_right(p,t) for p in prefixes)
            coupling[I]=coupling.get(I,Fraction(0))+hi-lo
        result['primal']=coupling
    return result
