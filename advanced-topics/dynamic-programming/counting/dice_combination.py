
MOD = 1000000007
dp = [0] * (1000010)
def count(n):
    
    dp[0] = 1
    
    for i in range(1, n+1):
        for j in range(1, 7):
            if i-j < 0:
                break

            dp[i] = (dp[i]%MOD + dp[i-j]%MOD)%MOD 
    return dp[n]%MOD;

n = int(input())
print(count(n))