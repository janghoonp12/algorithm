from collections import deque

N, M = map(int, input().split())
arr = [input() for i in range(N)]
visited = [[False for i in range(M)] for j in range(N)]
area = [[(0, 0) for i in range(M)] for j in range(N)]
ans = [[0 for i in range(M)] for j in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
area_idx = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] != '0' or visited[i][j]:
            continue
        que = deque()
        que.append((i, j))
        visited[i][j] = True
        cnt = 1
        temp = [(i, j)]
        area_idx += 1
        while len(que) > 0:
            x, y = que[0]
            que.popleft()
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny] or arr[nx][ny] != '0':
                    continue
                
                que.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
                temp.append((nx, ny))
        
        for k, l in temp:
            area[k][l] = (area_idx, cnt)


visited_area = [False for i in range(area_idx + 1)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == '0':
            continue
        A = 1
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if not (0 <= nx < N and 0 <= ny < M) or visited_area[area[nx][ny][0]]:
                continue
            A += area[nx][ny][1]
            visited_area[area[nx][ny][0]] = True
        ans[i][j] = A % 10
        
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            visited_area[area[nx][ny][0]] = False

for i in ans:
    for j in i:
        print(j, end='')
    print()