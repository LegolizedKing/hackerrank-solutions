
from itertools import permutations
S,a=input().split()
S=sorted(S)
k=int(a)
l=list(permutations(S,k))
r=list(map("".join, l))
for _ in r:
    print(_)
