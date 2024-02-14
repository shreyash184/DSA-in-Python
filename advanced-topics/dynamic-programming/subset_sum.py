

def subset(n, target):
    dp = [[0] * (target+1) for _ in range(n+1)]
    
    for i in range(0, n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, target + 1):
            dp[i][j] = dp[i-1][j]
            if arr[i-1] <= j:
                dp[i][j] = dp[i][j] or dp[i-1][j-arr[i-1]]
    for lst in dp:
        print(lst)
    return dp[n][target]



n = 6
target = 9
arr = [3, 34, 4, 12, 5, 2]
print(subset(n, target))
