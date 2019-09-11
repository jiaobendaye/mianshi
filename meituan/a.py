# -*- coding: utf-8 -*-
# import sys
# team = []
# while True:
#     line = sys.stdin.readline().strip()
#     if line=='':
#         break
#     item = line.split()
#     item = [int(i) for i in item]
#     team.append(item)
# print(team)

# n = team[0][0]
# nums1 = team[1]
# m = team[2][0]
# nums2 = team[3]
# print(nums1)
# str1 = ''.join(nums1)
# str2 = ''.join(nums2)
# def helper(a, b):
#     if a is '' or b is '':
#         return ''
#     elif a[-1] is b[-1]:
#         return helper(a[:-1], b[:-1]) + a[-1]
#     else:
#         sol_a = helper(a[:-1], b)
#         sol_b = helper(a, b[:-1])
#         if len(sol_a) > len(sol_b):
#             return sol_a
#         return sol_b
# print(helper(str1, str2))

team = []
with open('./in.txt') as f:
    data = f.readlines()
    for line in data:
        item = [int(i) for i in line.split()]
        team.append(item)
# print(team)
n = team[0][0]
nums1 = team[1]
m = team[2][0]
nums2 = team[3]
print(n, nums1, m, nums2)

dp =[[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if nums1[i-1] == nums2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp)
print(dp[n][m])
