from collections import defaultdict
n,m=map(int,input().split())
d=defaultdict(list)
for i in range(n):
    a=input()
    d[a].append(i+1)
for i in range(m):
    b=input()
    if len(d[b])>0:
        print(*d[b])
    else:
        print(-1)



