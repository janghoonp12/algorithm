from collections import deque


N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            start = (i, j)
            arr[i][j] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
size = 2
fish = 0
time = 0

while True:
    que = deque()
    visited = [[False for i in range(N)] for j in range(N)]
    dist = [[0 for i in range(N)] for j in range(N)]
    eat = False
    move = 500
    tx = ty = 20
    
    que.append((start))
    visited[start[0]][start[1]] = True
    while len(que) > 0:
        x, y = que[0]
        que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < N and 0 <= ny < N) or arr[nx][ny] > size or visited[nx][ny]:
                continue
            
            que.append((nx, ny))
            visited[nx][ny] = True
            dist[nx][ny] = dist[x][y] + 1
            
            if 0 < arr[nx][ny] < size:
                eat = True
                if dist[nx][ny] < move:
                    move = dist[nx][ny]
                    tx, ty = nx, ny
                elif dist[nx][ny] == move:
                    if nx < tx:
                        tx, ty = nx, ny
                    elif nx == tx:
                        ty = min(ty, ny)
    
    if eat:
        time += move
        fish += 1
        if fish == size:
            size += 1
            fish = 0
        start = (tx, ty)
        arr[tx][ty] = 0
    else:
        break
    
print(time)