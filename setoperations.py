n = int(input())
s = set(map(int, input().split()))
m=int(input())
for i in range(m):
    query=input().split()
    if query[0]=='pop':
        s.pop()
    elif query[0]=='remove':
        item=int(query[1])
        s.remove(item)
    elif query[0]=='discard':
        item=int(query[1])
        s.discard(item)
print(sum(list(s)))
