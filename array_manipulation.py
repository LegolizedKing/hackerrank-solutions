n=5
c=[0]*n
q=[[1,2,100],[2,5,100],[3,4,100]]

for i in range(len(q)):
	a=q[i][0]-1
	b=q[i][1]-1
	k=q[i][2]
	c+=c[a:b+1]+[k]
	print(c)
	
		

