from sys import stdin
I = stdin.readline

N = int(input())
arr = [[0]*(N+1)] + [[0] + list(map(int, I().split())) for _ in range(N)]
prefix = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix[i][j] = arr[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

ans = 0
for c in range(1, N):
    for d in range(1, N):
        TL = {}
        for a in range(c):
            for b in range(d):
                area = prefix[c][d] - prefix[c][b] - prefix[a][d] + prefix[a][b]
                TL[area] = TL.get(area, 0) + 1
        for e in range(c+1, N+1):
            for f in range(d+1, N+1):
                area = prefix[e][f] - prefix[e][d] - prefix[c][f] + prefix[c][d]
                ans += TL.get(area, 0)
                
        TR = {}
        for e in range(c+1, N+1):
            for b in range(d):
                area = prefix[e][d] - prefix[e][b] - prefix[c][d] + prefix[c][b]
                TR[area] = TR.get(area, 0) + 1
        for a in range(c):
            for f in range(d+1, N+1):
                area = prefix[c][f] - prefix[c][d] - prefix[a][f] + prefix[a][d]
                ans += TR.get(area,0)

print(ans)