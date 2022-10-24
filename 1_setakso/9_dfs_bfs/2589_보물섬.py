from collections import deque


N, M = map(int, input().split())
arr = [input() for i in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'W':
            continue

        que = deque()
        visited = [[False for i in range(M)] for j in range(N)]
        dist = [[0 for i in range(M)] for j in range(N)]
        
        que.append((i, j))
        visited[i][j] = True
        while len(que) > 0:
            x, y = que[0]
            que.popleft()
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny] or arr[nx][ny] == 'W':
                    continue
                
                que.append((nx, ny))
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                ans = max(ans, dist[nx][ny])

print(ans)