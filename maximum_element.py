stack=[]
n=int(input())
for i in range(n):
 a=input()
 cmd=a[0]
 if cmd=='1':
   q,value=map(int,a.split())
   stack.append(value) 
 elif cmd=='2':
   stack.pop()
 elif cmd=='3':
   print(max(stack))
 
