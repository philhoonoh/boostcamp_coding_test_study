import sys

n = int(sys.stdin.readline().rstrip())

dp = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(0, n)]

for row in range(n-2, -1, -1):
    for col in range(0, row + 1):
        dp[row][col] = dp[row][col] + max(dp[row+1][col], dp[row+1][col+1])

print(dp[0][0])