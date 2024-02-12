
def frog(nums, n):
    dp[0] = 0
    dp[1] = 0
    dp[2] = abs(nums[2] - nums[1])
    for i in range(3, n+1):
        dp[i] = min(dp[i-1] + abs(nums[i] - nums[i-1]), dp[i-2]+ abs(nums[i] - nums[i-2]))
    return dp[n];



n = int(input())
nums = []
nums.append(0)

dp = [0] * (n+1)

lst = list(map(int, input().split()))
for num in lst:
    nums.append(num)

print(frog(nums, n))