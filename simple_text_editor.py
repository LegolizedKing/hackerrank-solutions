t=int(input())
s=""
stack=[]
stack.append(s)
i=1
for _ in range(t):
    num=list(input().split())
    if int(num[0])==1:
        s+=str(num[1])
        stack.append(s)
        i+=1
    elif int(num[0])==2:
        a=int(num[1])
        s=s[:-a]
        stack.append(s)
        i+=1
    elif int(num[0])==3:
        a=int(num[1])
        print(s[a-1])
    elif int(num[0])==4:
        stack.pop()
        i-=1
        s=stack[i-1]
       
