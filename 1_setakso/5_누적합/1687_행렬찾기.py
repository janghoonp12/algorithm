from sys import stdin
I = stdin.readline

N, M = map(int, I().split())
arr = [[0]*(M+1)]+[[0]+list(map(int, input())) for _ in range(N)]

prefix = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        prefix[i][j] = arr[i][j] + prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1]

ans = 0
x = N
y = 1
while x>0:
    t = 0
    for i1 in range(0, N-y+1):
        if t == 1: break
        i2 = i1 + y
        for j1 in range(0, M-x+1):
            j2 = j1 + x
            if prefix[i2][j2] - prefix[i1][j2] - prefix[i2][j1] + prefix[i1][j1] == 0:
                ans = max(ans, x*y)
                y+=1
                t = 1
                break
    else:
        x-=1

print(ans)