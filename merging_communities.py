l=list(input().split())
n=[1]*l[0]
for _ in range(l[1]):
    m=list(input().split())
    a=m[1]
    c=m[2]
    if m[0]=='Q':
        print(n[a])
    elif m[0]=='M':
        b=[]
        b.append(a)
        b.append(b)

