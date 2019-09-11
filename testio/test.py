# -*- coding: utf-8 -*-

with open('./in.txt', 'r') as f:
    data = f.readlines()

    team = []
    for line in data:
        # print(line)
        item = line.split()
        # item = map(int item)
        item = [int(i) for i in item]
        team.append(item)
print(team)

# while True:
#     line = stdin.readline().strip()
#     if line=='':
#         break
#     item = line.split()
#     item = [int(i) for i in item]
#     team.append(item)
