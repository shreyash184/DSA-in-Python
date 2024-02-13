

import sys

def f(i, j):
    dp = [[0] * n for _ in range(n+2)]
    for i in range(n):
        dp[i][i] = nums[i]
    for len in range(2, n+1):
        for i in range(0, n-len+1):
            j = i+len-1
            if len == 2:
                dp[i][j] = max(nums[i], nums[j])
                continue
            x = dp[i+2][j]
            y = dp[i+1][j-1]
            z = dp[i][j-2]
            dp[i][j] = max(nums[i]+min(x,y), nums[j]+min(y,z))
    return dp[0][n-1]

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

# dp = []

# for i in range(n+50):
#     dp.append([-1] * (n+50))

print(f(0, n-1))