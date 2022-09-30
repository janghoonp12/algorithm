def dfs(x, y):
    global cnt

    cnt += 1
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny] or arr[nx][ny] == '0':
            continue
        
        dfs(nx, ny)


N = int(input())
arr = [input() for i in range(N)]
visited = [[False for i in range(N)] for j in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

apt = []
for i in range(N):
    for j in range(N):
        if visited[i][j] or arr[i][j] == '0':
            continue
        
        cnt = 0
        dfs(i, j)
        apt.append(cnt)

apt.sort()
print(len(apt))
for i in apt:
    print(i)