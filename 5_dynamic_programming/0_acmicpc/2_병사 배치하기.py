N = int(input())
soldier_lst = list(map(int, input().split()))

dp = [1] * N
soldier_lst = soldier_lst[::-1]

for i in range(1, N):
    for j in range(0, i):
        if soldier_lst[i] > soldier_lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))
