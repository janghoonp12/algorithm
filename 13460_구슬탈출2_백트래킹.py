def move(x, y, d):
    nx = x + dx[d]
    ny = y + dy[d]
    if arr[nx][ny] == 'O':
        return nx, ny
    if arr[nx][ny] == '#':
        return x, y
    return move(nx, ny, d)


def recur(cur, rx, ry, bx, by):
    global ans

    if cur == 11 or cur == ans:
        return
    
    if arr[bx][by] == 'O':
        return
    
    elif arr[rx][ry] == 'O':
        ans = min(ans, cur)
        return
    
    for i in range(4):
        nrx, nry = move(rx, ry, i)
        nbx, nby = move(bx, by, i)
        if nrx == nbx and nry == nby:
            if arr[nrx][nry] == 'O':
                pass
            elif i == 0:
                if rx > bx:
                    nbx -= dx[i]
                else:
                    nrx -= dx[i]
            elif i == 2:
                if rx < bx:
                    nbx -= dx[i]
                else:
                    nrx -= dx[i]
            elif i == 1:
                if ry > by:
                    nby -= dy[i]
                else:
                    nry -= dy[i]
            else:
                if ry < by:
                    nby -= dy[i]
                else:
                    nry -= dy[i]
        recur(cur + 1, nrx, nry, nbx, nby)


N, M = map(int, input().split())
arr = [input() for i in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            rx, ry = i, j
        elif arr[i][j] == 'B':
            bx, by = i, j

ans = 11

recur(0, rx, ry, bx, by)

if ans == 11:
    ans = -1

print(ans)