from collections import deque


N, M = map(int, input().split())
arr = [input() for i in range(N)]
que = deque()
visited = [[False for i in range(M)] for j in range(N)]
dist = [[1 for i in range(M)] for j in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

que.append((0, 0))
visited[0][0] = True
while len(que) > 0:
    x, y = que[0]
    que.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny] or arr[nx][ny] == '0':
            continue
        
        que.append((nx, ny))
        visited[nx][ny] = True
        dist[nx][ny] = dist[x][y] + 1

print(dist[N - 1][M - 1])