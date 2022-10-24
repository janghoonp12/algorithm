from collections import deque


dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

T = int(input())
for t in range(T):
    I = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    que = deque()
    visited = [[False for i in range(I)] for j in range(I)]
    dist = [[0 for i in range(I)] for j in range(I)]
    
    que.append((sx, sy))
    visited[sx][sy] = True
    while len(que) > 0:
        x, y = que[0]
        que.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < I and 0 <= ny < I) or visited[nx][ny]:
                continue
            
            que.append((nx, ny))
            visited[nx][ny] = True
            dist[nx][ny] = dist[x][y] + 1
            
        if visited[ex][ey]:
            break
    
    print(dist[ex][ey])