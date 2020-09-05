arr=[1,2,3,9,10,12]
flag=0
d=0
T=True
while(T):
  t=1*arr[0]+2*arr[1]
  arr.remove(arr[0])
  arr.remove(arr[0]) 
  arr.append(t)
  arr=sorted(arr)
  print(arr)
  d+=1
  if all(arr) >=7:
    flag=1
    T=False
if flag==0:
 print(-1)
else:
 print(d)
 
