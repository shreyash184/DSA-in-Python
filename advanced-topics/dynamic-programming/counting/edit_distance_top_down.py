

def f(s1, s2, i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    if s1[i] == s2[j]:
        dp[i][j] = f(s1, s2, i-1, j-1)
        return dp[i][j]

    replace = f(s1, s2, i-1, j-1)
    insert = f(s1, s2, i, j-1)
    delete = f(s1, s2, i-1, j)

    dp[i][j] = 1 + min(replace, insert, delete)

    return dp[i][j]


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

print(f(s1, s2, n, m))
# print(dp)