from math import sqrt


def recur(cur, x, y, pcnt, mcnt):
    global ans
    
    if pcnt > N // 2 or mcnt > N // 2:
        return
    
    if cur == N:
        ans = min(ans, sqrt(x * x + y * y))
        return
    
    recur(cur + 1, x + arr[cur][0], y + arr[cur][1], pcnt + 1, mcnt)
    recur(cur + 1, x - arr[cur][0], y - arr[cur][1], pcnt, mcnt + 1)


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    ans = float('INF')
    visited = [False for i in range(N)]
    recur(0, 0, 0, 0, 0)
    print(ans)