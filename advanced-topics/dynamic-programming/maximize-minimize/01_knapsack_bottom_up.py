


def knapsack(n, Mw):

    for i in range(1, n+1):
        for j in range(1, Mw+1):
            dp[i][j] = dp[i-1][j]
            if w[i] <= j:
                dp[i][j] = max(dp[i][j], v[i] + dp[i-1][j-w[i]])
    return dp[n][Mw]
    


w = [0, 3, 4, 5]
v = [0, 3, 5, 6]
capacity = 8
dp = [[0] * 500 for _ in range(10000)]
print(knapsack(len(w)-1, capacity))