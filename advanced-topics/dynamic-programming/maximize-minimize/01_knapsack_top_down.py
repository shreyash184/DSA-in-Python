


def knapsack(i, j):
    if i == 0 or j == 0:
        dp[i][j] = 0
        return dp[i][j]
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    result = 0;
    if w[i] <= j:
        pick = v[i] + knapsack(i-1, j-w[i])
        not_pick = knapsack(i-1, j)
        result = max(pick, not_pick)
    else:
        not_pick = knapsack(i-1, j)
        result = not_pick
    
    dp[i][j] = result 
    return dp[i][j]
    


w = [0, 3, 4, 5]
v = [0, 3, 5, 6]
capacity = 8
dp = [[-1] * 500 for _ in range(10000)]
print(knapsack(len(w)-1, capacity))