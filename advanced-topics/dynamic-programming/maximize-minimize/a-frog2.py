
def frog(nums, n):
    dp = [2**31-1] * (n+1)
    dp[1] = 0
    for i in range(2, n+1):
        for j in range(1, k+1):
            if i-j >= 0:
                dp[i] = min(dp[i-j] + abs(nums[i] - nums[i-j]), dp[i])
    return dp[n];



n, k = list(map(int, input().split()))
# print(n, k)
nums = []
nums.append(0)




lst = list(map(int, input().split()))
for num in lst:
    nums.append(num)

print(frog(nums, n))