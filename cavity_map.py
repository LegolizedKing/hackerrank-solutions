def cavityMap(grid,n):
	for i in range(1,n-1):
        	for j in range(1,n-1):
            		if grid[i-1][j]!='X' and int(grid[i-1][j]) < int(grid[i][j]) and \
                	grid[i+1][j]!='X' and int(grid[i+1][j]) < int(grid[i][j]) and \
                	grid[i][j-1]!='X' and int(grid[i][j-1]) < int(grid[i][j]) and \
                	grid[i][j+1]!='X' and int(grid[i][j+1]) < int(grid[i][j]):
	                    	grid[i][j]='X'
n=int(input())
grid=[]
for _ in range(n):
   grid_item=list(input())
   grid.append(grid_item)
cavityMap(grid,n)
for i in grid:
	l=''.join(i)
	print(l)
