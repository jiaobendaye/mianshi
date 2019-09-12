# -*- coding: utf-8 -*-

# with open('./in.txt', 'r') as f:
#     data = f.readlines()

#     team = []
#     for line in data:
#         # print(line)
#         item = line.split()
#         # item = map(int item)
#         item = [int(i) for i in item]
#         team.append(item)
# print(team)

# while True:
#     line = stdin.readline().strip()
#     if line=='':
#         break
#     item = line.split()
#     item = [int(i) for i in item]
#     team.append(item)



while 1:
    nm = list(map(int, input().split(' ')) )
    n = nm[0]
    m = nm[1]
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    print(' '.join(str(i) for i in sorted(set(A+B))))
          