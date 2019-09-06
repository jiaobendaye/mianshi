import heapq
import numpy as np 

a = raw_input()
n, m, k = a.split() 
n = eval(n)
m = eval(m)
k = eval(k)

grid = np.zeros((n, m),int)

for i in range(n):
    for j in range(m):
        grid[i][j] = (i+1) * (j+1)

List = grid.flatten()
pool = heapq.nlargest(k, List)
result = pool[-1]
print(result)