# -*- coding: utf-8 -*-
solutionOfN = []
def fun1(n, k):      

    dfs(n, '', 0, k)
    return len(solutionOfN)
def dfs(n, curr, long_count, k):
    if n == 1:
        solutionOfN = ['0', '1']
        return
    if long_count == k:
        return

    if len(curr) == n:
        solutionOfN.append(curr)
        return
    if curr is '':
        dfs(n, curr+'1', long_count+1, k)
        dfs(n, curr+'0', long_count+1, k)
    else:
        if curr[-1] is '1':
            dfs(n, curr+'1', long_count+1, k)
            dfs(n, curr+'0', 0, k)
        if curr[-1] is '0':
            dfs(n, curr+'1', 0, k)
            dfs(n, curr+'0', long_count+1, k)  
print(fun1(5, 2))
