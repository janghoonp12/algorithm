# import sys
# sys.stdin = open('input.txt', 'r')

def increase(c, i, j):
    global inc
    
    visited[i][j] = True
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        y = i + di
        x = j + dj
        if not 0 <= y < N or not 0 <= x < N:
            continue
        if arr[y][x] == arr[i][j] + 1:
            increase(c + 1, y, x)
            break
    else:
        inc = c

def decrease(c, i, j):
    global dec
    
    visited[i][j] = True
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        y = i + di
        x = j + dj
        if not 0 <= y < N or not 0 <= x < N:
            continue
        if arr[y][x] == arr[i][j] - 1:
            decrease(c + 1, y, x)
            break
    else:
        dec = (c, i, j)

def count_moves():
    global inc, dec

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            increase(0, i, j)
            decrease(0, i, j)
            
            if ans[1] < inc + dec[0] + 1:
                ans[0] = arr[dec[1]][dec[2]]
                ans[1] = inc + dec[0] + 1
            elif ans[1] == inc + dec[0] + 1:
                ans[0] = min(ans[0], arr[dec[1]][dec[2]])


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    visited = [[False] * N for i in range(N)]
    inc = 0
    dec = 0
    ans = [1, 1]
    count_moves()
    
    print(f'#{t}', *ans)