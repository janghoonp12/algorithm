<<<<<<< HEAD
import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline
print = sys.stdout.write


def dfs(cur, prv):
    color_cnt[cur][arr[cur]] += 1               
    for nxt in v[cur]:
        if nxt == prv:
            continue
        
        parent[nxt] = cur
        dfs(nxt, cur)
        for i in range(2):
            color_cnt[cur][i] += color_cnt[nxt][i]


N = int(input())
arr = [-1] + list(map(int, input().split()))
v = [[] for i in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

color_cnt = [[0] * 2 for i in range(N + 1)]
parent = [0 for i in range(N + 1)]

dfs(1, 0)


Q = int(input())
for i in range(Q):
    q = int(input())
    ans = 0
    
    C = len(v[q])
    blue = []
    red = []
    for j in v[q]:
        if j == parent[q]:
            continue
        ans -= color_cnt[j][0] * color_cnt[j][1]
        if color_cnt[j][0]:
            blue.append(color_cnt[j][0])
        if color_cnt[j][1]:
            red.append(color_cnt[j][1])
    ans -= (color_cnt[1][0] - color_cnt[q][0]) * (color_cnt[1][1] - color_cnt[q][1])
    blue.append(color_cnt[1][0] - color_cnt[q][0])
    red.append(color_cnt[1][1] - color_cnt[q][1])
    
    for j in range(len(blue)):
        for k in range(len(red)):
            ans += blue[j] * red[k]
    print(f'{ans}\n')
=======
from collections import deque


N, M, F = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
x, y = map(int, input().split())
passenger = [list(map(int, input().split())) for i in range(M)]

x -= 1
y -= 1
for i in range(M):
    passenger[i][0] -= 1
    passenger[i][1] -= 1
    passenger[i][2] -= 1
    passenger[i][3] -= 1

dist = [[[-1 for i in range(N)] for j in range(N)] for k in range(M)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(M):
    visited = [[False for j in range(N)] for k in range(N)]
    
    que = deque()
    px = passenger[i][0]
    py = passenger[i][1]
    dist[i][px][py] = 0
    
    que.append((px, py))
    visited[px][py] = True
    while len(que) > 0:
        cx, cy = que[0]
        que.popleft()
        
        for j in range(4):
            nx = cx + dx[j]
            ny = cy + dy[j]
            if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny] or arr[nx][ny]:
                continue
            que.append((nx, ny))
            visited[nx][ny] = True
            dist[i][nx][ny] = dist[i][cx][cy] + 1

for i in range(M):
    if dist[i][x][y] == -1 or dist[i][passenger[i][2]][passenger[i][3]] == -1:
        print(-1)
        quit()

ans = -1
moved = [0 for i in range(M)]
while True:
    m = float('INF')
    for i in range(M):
        if moved[i]:
            continue
        
        if dist[i][x][y] < m:
            m = dist[i][x][y]
            idx = i
        elif dist[i][x][y] == m:
            if passenger[i][0] < passenger[idx][0]:
                idx = i
            elif passenger[i][0] == passenger[idx][0]:
                if passenger[i][1] < passenger[idx][1]:
                    idx = i
    
    d = dist[idx][passenger[idx][2]][passenger[idx][3]]
    total_move = m + d
    if total_move > F:
        break
    
    F = F - m + d
    x = passenger[idx][2]
    y = passenger[idx][3]
    moved[idx] = 1
    
    if min(moved):
        ans = F
        break

print(ans)
>>>>>>> 2165fb1e2f9c925090a7a9747cf76ec934541e81
