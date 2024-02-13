



def f(i, j):
    if j-i == 0:
        return nums[i]
    if j-i == 1:
        return max(nums[i], nums[j])
    
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = max(nums[i] + min(f(i+2, j), f(i+1, j-1)), nums[j] + min(f(i+1, j-1), f(i, j-2)))
    return dp[i][j]


n = int(input())
nums = list(map(int, input().split()))

dp = []

for i in range(n+50):
    dp.append([-1] * (n+50))

print(f(0, n-1))