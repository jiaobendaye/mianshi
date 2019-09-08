import sys
from sys import stdin
from bisect import bisect
    
# team = []
# while True:
#     line = stdin.readline().strip()
#     if line=='':
#         break
#     item = line.split()
#     item = [int(i) for i in item]
#     team.append(item)

# N = team[0][0]
# A = team[1]
# print(N)
# print(A)

N = 4
A = [1, 1, 0]

def samller(keep, i):
    if not keep: return None
    for num in keep:
        if num < i:
            return num
    return None
def bigger(keep, i):
    if not keep: return None
    for num in keep:
        if num > i:
            return num
    return None
def dfs(i, cur, keep):
    print(i, cur, result, keep)
    if len(cur) is N:
        result.append(cur)
        print('count++')
        return
    if A[len(cur)]:
        j = samller(keep, i)
        if not j:
            return
        else:
            dfs(j, cur.append(i), keep.remove(i))
    else:
        j = bigger(keep, i)
        if not j:
            return
        else:
            dfs(j, cur.append(i), keep.remove(i))
        
    
listOfN = list(range(1, N+1))
print(listOfN)
result = []

for i in listOfN:
	dfs(i, [], listOfN.remove(i))

# sys.stdout(len(result) %(10^9 + 7))
print(result)