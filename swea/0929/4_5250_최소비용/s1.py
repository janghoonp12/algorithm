from collections import deque


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    cost = [[float('inf') for i in range(N)] for j in range(N)]
    
    cost[0][0] = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    que = deque()
    que.append((0, 0))

    while len(que) > 0:
        x, y = que[0]
        que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < N):
                continue
            
            temp = cost[x][y] + 1 + max(arr[nx][ny] - arr[x][y], 0)
            if temp < cost[nx][ny]:
                cost[nx][ny] = temp
                que.append((nx, ny))
    
    for i in cost:
        print(i)
    
    ans = cost[N - 1][N - 1]
    
    print(f'#{t}', ans)


'''

1
5
0   25  25  25  25
0   25  0   0   0
0   25  0   25  0
0   0   0   25  0
25  25  25  25  0


'''