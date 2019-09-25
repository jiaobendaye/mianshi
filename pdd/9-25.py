from collections import Counter 
from sys import stdin
import heapq
stdin = open('./in.txt','r')
team = []
while True:
    line = stdin.readline().strip()
    if line=='':
        break
    item = line.split()
    item = [int(i) for i in item]
    team.append(item)
print(team)
n = team[0][0]
m = team[0][1]
data = team[1]

#count 0
count = Counter(data)
coount0 =  count[0]
m = m - coount0
if m <= 0: 
    print('res:',0) 
#remove 0
data = [i for i in data if i]
res = 0
sorted(data)
data= data[:(2*m)]
for i in range(m):
    a = data[i]
    b = data[2*m-i-1]
    time = a*b
    res += time
print('res:',res)