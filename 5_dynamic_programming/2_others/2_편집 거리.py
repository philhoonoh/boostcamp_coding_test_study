import sys

word_1 = str(sys.stdin.readline().rstrip())
word_2 = str(sys.stdin.readline().rstrip())

n = len(word_1)
m = len(word_2)

dp = [[0] * (m+1) for _ in range(n + 1)]

for col in range(m+1):
    dp[0][col] = col

for row in range(n+1):
    dp[row][0] = row

for row in range(1, n+1):
    for col in range(1, m+1):
        if word_1[row-1] == word_2[col-1]:
            dp[row][col] = dp[row-1][col-1]
        else:
            dp[row][col] = 1 + min(dp[row-1][col], dp[row-1][col-1], dp[row][col-1])

print(dp[n][m])