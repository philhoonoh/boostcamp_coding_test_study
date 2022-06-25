import sys

t = int(sys.stdin.readline().rstrip())

result = []
for _ in range(0,t):
    n, m = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))

    dp = []
    for i in range(n):
        dp.append(arr[i * m:i * m + m])

    for col in range(1,m):
        for row in range(0,n):
            left_up = dp[row-1][col-1] if row - 1 > 0 else 0
            left = dp[row][col-1]
            left_down = dp[row+1][col-1] if row + 1 < n else 0
            dp[row][col] = dp[row][col] + max(left_up, left,  left_down)

    max_ = 0
    for x in range(0, n):
        max_ = max(dp[x][-1], max_)
    result.append(max_)

for output in result:
    print(output)