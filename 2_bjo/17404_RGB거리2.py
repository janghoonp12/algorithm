from sys import stdin
input = stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
ans = float('INF')
for i in range(3):
    dp = [[0 for i in range(3)] for j in range(N)]
    dp[1] = arr[1][:]
    dp[1][i] = float('INF')
    
    for j in range(2, N):
        dp[j][0] = arr[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = arr[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = arr[j][2] + min(dp[j - 1][1], dp[j - 1][0])
    
    dp[N- 1][i] = float('INF')
    ans = min(ans, arr[0][i] + min(dp[N - 1]))
print(ans)