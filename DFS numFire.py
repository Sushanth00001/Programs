def numFire(grid, i, j):
    if not grid:
        return 0
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!='1':
        return
    grid[i][j]='2'
    numFire(grid,i+1,j)
    numFire(grid,i-1,j)
    numFire(grid,i,j+1)
    numFire(grid,i,j-1)
    
grid=[
['1','1','1','1','0'],
['1','1','0','0','1'],
['0','0','1','0','0'],
['0','0','0','1','1'],
]
numFire(grid, 0, 0)
count=0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]=='1':
            count+=1
print(count)