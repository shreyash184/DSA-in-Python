def f(x, k, l, dp):
    if x < 0:
        return 1
    if x == 0:
        return 0
    if (x == 1 or x == k or x == l):
        return 1
    
    if dp[x] != -1:
        return dp[x]
    
    dp[x] = not(f(x-1, k, l, dp) and f(x-k, k, l, dp) and f(x-l, k, l, dp))
    
    return dp[x]




t, k, l = list(map(int, input().split()))
dp = [-1] * (1000006)

f(1000000, k, l, dp)

nums = list(map(int, input().split()))

for num in nums:
    if dp[num] == 1:
        print("A", sep=" ")
    else:
        print("B", sep=" ")

