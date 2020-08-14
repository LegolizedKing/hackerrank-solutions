
N,K=map(int,input().split())
A = list(map(int,input().strip().split()))[:N]
count=0
for i in range(N):
	x=A[i]
	a=x-K
	b=x+K
	c=any(j!=x and j>=a and j<=b for j in A)
	print(c)
	if c:
		count+=1
print(count)
