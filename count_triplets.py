from itertools import combinations

arr=[1,5,5,25,125]
count=0
r=5
l=list(combinations(arr,3))
#for i in range(len(l)):
#	if l[i][2]/l[i][1]==l[i][1]/l[i][0]==r:
#		count+=1
print(l)

