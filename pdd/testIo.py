import heapq
import sys

# nums = [134234, 3522, 45134, 6534, 76, 234, 23, 363, 78675, 234, 563]
# N = 5

# s = raw_input()
# nums_str,N_str=s.split(';')

# nums = eval(nums_str)
# N = eval(N_str)
line = sys.stdin.readline().strip()

line = line.split(';')
print(line[0])
print(line[1])
data = eval(line[0])
N = eval(line[1])
print(data, N)