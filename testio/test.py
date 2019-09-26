# -*- coding: utf-8 -*-
from sys import stdin
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
# team = []
# stdin =  open('./in.txt', 'r')
# while True:
#     line = stdin.readline().strip()
#     if line=='':
#         break
#     item = line.split()
#     item = [int(i) for i in item]
#     team.append(item)
# print(team)
"""
3
2
23 43  
4 
34 654 65 34
1
234
"""
def solve(nums):
    print(nums)
c = int(stdin.readline().strip())
for _ in range(c):
    a = int(stdin.readline().strip())
    nums = list(map(int, stdin.readline().strip().split()))
    solve(nums)

# res = []
# # stdin = open('./in.txt', 'r')
# def solve(A, B):
#     return sorted(set(A+B))
# while 1:
#     nm = stdin.readline().strip()
#     if nm is '':
#         break
#     nm = [int(i) for i in nm.split()]
#     n = nm[0]
#     m = nm[1]
#     A = list(map(int,stdin.readline().strip().split()))
#     B = list(map(int,stdin.readline().strip().split()))
#     res.append(solve(A, B))
# print(res)
# for item in res:
#     print(' '.join(str(i) for i in item))


          