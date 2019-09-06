from sys import stdin
# nums = [5,1,4,2,3]
line = stdin.readline().strip()
nums = eval(line)

def length_of_lis(nums):
    len_nums = len(nums)
    if len_nums is 0:
        return 0
    
    dp = [1] * len_nums
    for i in range(len_nums - 1):
        for j in range(i + 1):
            if nums[i+1] > nums[j]:
                dp[i+1] = max(dp[i+1], dp[j]+1)
    return max(dp)
    
res = length_of_lis(nums)
print(res)