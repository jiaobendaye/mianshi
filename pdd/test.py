import heapq
import sys

# nums = [134234, 3522, 45134, 6534, 76, 234, 23, 363, 78675, 234, 563]
# N = 5

# s = raw_input()
# nums_str,N_str=s.split(';')

# nums = eval(nums_str)
# N = eval(N_str)
line = sys.stdin.readline().split()
line = line.split(';')

data = eval(line[0])
N = eval(line[1])

pool = heapq.nlargest(N, nums)
#pool[0] is the bigest on pool

# pool_sorted = sorted(pool)

pool_even = list(filter(lambda x: x%2==0, nums))
pool_odd = list(filter(lambda x: x%2==1, nums))

pool_even_sorted  = sorted(pool_even,reverse=True)
pool_odd_sorted = sorted(pool_odd,reverse=True)

result = pool_even_sorted + pool_odd_sorted
print(result)