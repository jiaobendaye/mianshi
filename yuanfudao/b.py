from sys import stdin
# NM = stdin.readline().strip().split()
# N = int(NM[0])
# M = int(NM[1])
# team = []
# for i in range(N):
#     item = stdin.readline().strip()
#     item = list(map(int, item.split()))
#     team.append(item)
# print(N,M)
# print(team)
N = 3
M =3
team = [[1, 2, 3], [4, 5,6], [7, 8, 9]]

result, i, j, di, dj = [], 0,0,1,0

for _ in range(N*M):
    result.append(team[i][j])
    team[i][j] = 0
    if team[(i+di)%N][(j+dj)%M] is 0:
        dj, di = di, -dj
    i += di
    j += dj

print(result)