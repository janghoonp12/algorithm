# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(input()) for i in range(N)]

    b = False
    for i in range(N):
        if b:
            break
        for j in range(N):
            if arr[i][j] == '2':
                s = (i, j)
                b = True
                break
    
    D = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    visited = [[0]*N for i in range(N)]
    queue = []
    queue.append(s)
    ans = 0
    fin = False
    while queue:
        if fin:
            break

        i, j = queue.pop(0)
        for di, dj in D:
            x = i + di
            y = j + dj
            if 0 <= x < N and 0 <= y < N:
                if arr[x][y] == '3':
                    ans = visited[i][j]
                    fin = True
                    break

                if not visited[x][y] and arr[x][y] == '0':
                    queue.append((x, y))
                    visited[x][y] = visited[i][j] + 1

    print(f'#{t} {ans}')