from sys import stdin
I = stdin.readline

def c_len(arr):
    s = 0
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                l = 100
                for k in arr:
                    l = min(l, abs(k[0] - i) + abs(k[1] - j))
                s += l
    return s

def recur(cur, start):
    global ans 

    if cur == M:
        ans = min(ans, c_len(arr))
        return
    
    for i in range(start, C):
        arr[cur] = chicken[i]
        recur(cur + 1, i + 1)


N, M = map(int, I().split())
city = [list(map(int, I().split())) for i in range(N)]
chicken = []
arr = [0 for i in range(M)]

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))
C = len(chicken)

ans = 10000
recur(0, 0)

print(ans)
