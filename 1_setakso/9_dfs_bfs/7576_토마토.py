from collections import deque


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]

que = deque()
visited = [[False for i in range(M)] for j in range(N)]
dist = [[0 for i in range(M)] for j in range(N)]
dx = [1, 0 ,-1, 0]
dy = [0, 1, 0 ,-1]
ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            que.append((i, j))
            visited[i][j] = True

while len(que) > 0:
    x, y = que[0]
    que.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny] or arr[nx][ny] == -1:
            continue
        
        que.append((nx, ny))
        visited[nx][ny] = True
        dist[nx][ny] = dist[x][y] + 1
        ans = dist[nx][ny]

for i in range(N):
    for j in range(M):
        if not arr[i][j] and not visited[i][j]:
            ans = -1
            
print(ans)