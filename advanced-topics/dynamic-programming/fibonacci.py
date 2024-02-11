n = 10
dp = [-1] * (n+1)

def fib(n):
    if n == 0 or n == 1:
        return n    
    if dp[n] != -1:
        return dp[n]
    
    ans = fib(n-1) + fib(n-2)
    return ans




print(fib(n))