def switch(x, y):
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < 10 and 0 <= ny < 10):
            continue
        if arr_light[nx][ny] == '#':
            arr_light[nx][ny] = 'O'
        else:
            arr_light[nx][ny] = '#'


def turn_lights(x, y, cnt):
    global ans
    
    if y == 10:
        turn_lights(x + 1, 0, cnt)
        return
    
    if x == 9:
        for i in range(10):
            if arr_light[9][i] != arr[9][i]:
                return
        ans = min(ans, cnt)
        return
    
    if arr_light[x][y] == arr[x][y]:
        turn_lights(x, y + 1, cnt)
    else:
        switch(x + 1, y)
        turn_lights(x, y + 1, cnt + 1)
        switch(x + 1, y)


def first_line(cur, cnt):
    if cur == 10:
        turn_lights(0, 0, cnt)
        return
    
    switch(0, cur)
    first_line(cur + 1, cnt + 1)
    switch(0, cur)
    
    first_line(cur + 1, cnt)


arr = [input() for i in range(10)]

arr_light = [['#' for i in range(10)] for j in range(10)]
dx = [-1, 0, 0, 0, 1]
dy = [0, -1, 0, 1, 0]
ans = float('INF')

first_line(0, 0)

if ans == float('INF'):
    print(-1)
else:
    print(ans)