
dp = [2**31-1] * (1000010)


def giveDigits(n):
    digits = []

    while n != 0:
        digits.append(n%10)
        n = int(n/10)
    digits.reverse()
    return digits

def count(n):
    dp[0] = 0
    for i in range(1, n+1):
        for digit in giveDigits(i):
            if i-digit < 0:
                break
            dp[i] = min(dp[i],dp[i-digit])
        dp[i] += 1
    return dp[n]

n = int(input())
print(count(n))
# print(giveDigits(234))