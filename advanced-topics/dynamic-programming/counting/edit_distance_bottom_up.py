


def f(s1, s2, i, j, dp):
    for i in range(len(s1)):
        dp[i][0] = i 
    for i in range(len(s2)):
        dp[0][i] = i 

    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                dp[i][j]  = dp[i-1][j-1]
                continue

            replace = dp[i-1][j-1] 
            insert = dp[i][j-1]
            delete = dp[i-1][j]
            dp[i][j] = 1 + min(replace, insert, delete)
    
    return dp[len(s1)-1][len(s2)-1]

word1 = "intention"
word2 = "execution"

n = len(word1)
m = len(word2)

s1 = " "
s2 = " "
s1 += word1
s2 += word2 

print(s1, s2)

dp = []

for i in range(n+1):
    dp.append([-1] * (m+1))

# dp.clear()

print(f(s1, s2, n, m, dp))