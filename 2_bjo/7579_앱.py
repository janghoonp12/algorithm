N, M = map(int, input().split())
mem = list(map(int, input().split()))
cost = list(map(int, input().split()))

C = sum(cost)
visited = [[False for i in range(N)] for j in range(C + 1)]
dp = [0 for i in range(C + 1)]
ans = 0

for i in range(N):
    if cost[i] == 0:
        dp[0] += mem[i]
        visited[0][i] = True

for i in range(1, C + 1):
    dp[i] = dp[i - 1]
    idx = -1
    idxx = -1
    for j in range(N):
        temp = i - cost[j]
        if temp < 0 or visited[temp][j] or cost[j] == 0:
            continue
        
        if dp[temp] + mem[j] > dp[i]:
            idx = temp
            dp[i] = dp[temp] + mem[j]
            idxx = j
    if idx == -1:
        visited[i] = visited[i - 1][:]
        continue
    visited[i] = visited[idx][:]
    visited[i][idxx] = True
    if dp[i] >= M:
        ans = i
        break

print(ans)