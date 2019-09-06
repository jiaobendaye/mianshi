from sys import stdin

team=[]
while True:
    line = stdin.readline().strip()
    if line=='':
        break
    item = line.split(' ')
    item = [int(i) for i in item]
    team.append(item)

t = team[0][0]
k = team[0][1]

result = []
for i in range(1, t+1):
    [a, b] = team[i]
    # print("[a, b] ==> ", (a, b))
    result.append(fn(a,b,k))

def fun1(n, k):

    def dfs(n, curr, long_count, k):
        if n = 1:
            solutionOfN = ['0', '1']
            return
        if long_count == k:
            return

        if len(curr) == n:
            solutionOfN.append(curr)
            return

        if curr[-1] is '1'：
            dfs(n, curr+'1', long_count+1, k)
            dfs(n, curr+'0', 0, k)
        if curr[-1] is '0':
            dfs(n, curr+'1', 0, k)
            dfs(n, curr+'0', long_count+1, k)        
    solutionOfN = []
    dfs(n, '', 0, k)
    return len(solutionOfN)


