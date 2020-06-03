import math
def pickingNumbers(a,n):
	b=[0]*100
	m=0
	for i in range(n):
		b[a[i]]=a.count(a[i])
	for j in range(1,100):
		t=(b[j]+b[j-1])
		m=max(m,t)
	return m
n=int(input())
a=list(map(int,input().rstrip().split()))
r=pickingNumbers(a,n)
print(r)
