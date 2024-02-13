def count(n, m):
    for i in range(n):
        if mat[i][0] == 1:
            break
        dp[i][0] = 1
    for i in range(m):
        if mat[0][i] == 1:
            break
        dp[0][i] = 1

    for i in range(1, n):
        for j in range(1, m):
            if mat[i][j] != 1:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
    return dp[n-1][m-1]



mat = [[0, 0, 0], 
       [0, 1, 0], 
       [0, 0, 0]]
dp = []

for i in range(len(mat)+1):
    dp.append([0] * (len(mat[0])+1))

print(count(len(mat), len(mat[0])))

