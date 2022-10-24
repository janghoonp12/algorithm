from sys import stdin
I = stdin.readline

N, M = map(int, I().split())
arr = [[0]*(M+1)]+[[0]+list(map(int, I().split())) for _ in range(N)]

prefix = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        prefix[i][j] = arr[i][j] + prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1]

ans = prefix[1][1]
for i1 in range(0, N):
    for i2 in range(i1+1, N+1):
        for j1 in range(0, M):
            for j2 in range(j1+1, M+1):
                ans = max(ans, prefix[i2][j2] - prefix[i1][j2] - prefix[i2][j1] + prefix[i1][j1])

print(ans)                