

# Problematic , Please fix this isse 
def knapsack(n, Mw, dp, dp1):

    for i in range(1, n+1):
        for j in range(1, Mw+1):
            dp1[i] = dp[i]
            if w[i] <= j:
                dp1[i] = max(dp1[i], v[i] + dp[j-w[i]])
        dp = dp1.copy()
        dp1 = [0] * (Mw+1)
        print(dp)
    return dp1[Mw]
    


w = [0, 3, 4, 5]
v = [0, 3, 5, 6]
capacity = 8
dp = [0] * (capacity+1)
dp1 = [0] * (capacity+1)

print(knapsack(len(w)-1, capacity, dp, dp1))
# print(dp1)