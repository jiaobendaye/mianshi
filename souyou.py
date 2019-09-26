n = 5
m = 15
#len(limit) == n
limit = [[1,3],[2,5],[1,6],[2, 6],[4,8]]
global res 
res = 0
state = dict((i,0)for i in range(n))
def dfs(curCom, state):
    if len(curCom) is m:
        res +=1
        return
    
    for i in range(n):
        if state[i] < limit[i]:
            state[i] +=1
            curCom.append(i)
            dfs(curCom, state)
        else: 
            break
print(dfs([],state))