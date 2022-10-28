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