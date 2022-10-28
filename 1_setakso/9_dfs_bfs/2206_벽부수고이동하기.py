from collections import deque


N, M = map(int, input().split())
arr = [input() for i in range(N)]
visited = [[[0, 0] for i in range(M)] for j in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

que = deque()
que.append((0, 0))
visited[0][0][0] = 1
while len(que) > 0:
    x, y = que[0]
    que.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        
        if arr[nx][ny] == '1':
            if not visited[x][y][0]:
                continue
            
            if visited[nx][ny][1] == 0 or visited[nx][ny][1] > visited[x][y][0] + 1:
                que.append((nx, ny))
                visited[nx][ny][1] = visited[x][y][0] + 1
        
        else:
            for j in range(2):
                if not visited[x][y][j]:
                    continue
                if visited[nx][ny][j] == 0 or visited[nx][ny][j] > visited[x][y][j] + 1:
                    que.append((nx, ny))
                    visited[nx][ny][j] = visited[x][y][j] + 1

a, b = visited[N - 1][M - 1]
if a and b:
    print(min(a, b))
elif a:
    print(a)
elif b:
    print(b)
else:
    print(-1)