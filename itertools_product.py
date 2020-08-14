from itertools import product

A=list(map(int,input().split()))
B=list(map(int,input().split()))

c=list(product(A,B))
print(*c)

