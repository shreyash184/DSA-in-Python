
dp = [2**31-1] * (1000005)

def count(n):
    dp[0] = 0
    for i in range(1, n+1):
        for coin in denomination:
            if i-coin >= 0:
                dp[i] = min(dp[i],1+dp[i-coin])
    return dp[n]

n, sum = list(map(int, input().split()))
denomination = list(map(int, input().split()))
ans = count(sum)
if ans == 2**31-1:
    print(-1)
else:
    print(ans)

# This solution is giving tle for 3 test case, not sure why, but the solution looks fine to me