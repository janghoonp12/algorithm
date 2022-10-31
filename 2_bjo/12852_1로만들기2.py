N = int(input())
dp = [[float('INF'), 0] for i in range(N + 1)]
dp[1] = [0, 0]
for i in range(2, N + 1):
    if i % 2 == 0 and dp[i // 2][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = i // 2
    
    if i % 3 == 0 and dp[i // 3][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 3][0] + 1
        dp[i][1] = i // 3
    
    if dp[i][0] > dp[i - 1][0]:
        dp[i][0] = dp[i - 1][0] + 1
        dp[i][1] = i - 1
print(dp[N][0])
while N:
    print(N, end = ' ')
    N = dp[N][1]
    