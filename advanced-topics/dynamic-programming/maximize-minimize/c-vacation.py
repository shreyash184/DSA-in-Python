def vacation(mat):
    n = len(mat)
    dp[0][0] = mat[0][0]
    dp[0][1] = mat[0][1]
    dp[0][2] = mat[0][2]

    for i in range(1, n):
        dp[i][0] = mat[i][0] + max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = mat[i][1] + max(dp[i-1][0], dp[i-1][2])
        dp[i][2] = mat[i][2] + max(dp[i-1][0], dp[i-1][1])

    return max(dp[n-1][0], dp[n-1][1], dp[n-1][2])

n = int(input())
mat = []
dp = []

for i in range(n):
    dp.append([0] * 3)

# print(dp)

for i in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

print(vacation(mat))
# print(dp)