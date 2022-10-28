from sys import stdin
I = stdin.readline

N = int(I())
arr = [[0]*(N+1)] + [[0] + list(map(int, I().split())) for _ in range(N)]
prefix = [[[0]*11 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, 11):
            prefix[i][j][k] = prefix[i][j-1][k] + prefix[i-1][j][k] - prefix[i-1][j-1][k]
        prefix[i][j][arr[i][j]] += 1
    
Q = int(input())
for _ in range(Q):
    x1, y1, x2, y2 = map(int, I().split())
    count = 0
    for i in range(1, 11):
        if prefix[x2][y2][i] - prefix[x2][y1-1][i] - prefix[x1-1][y2][i] + prefix[x1-1][y1-1][i]:
            count += 1
    print(count)