from copy import deepcopy


def move(fx, fy, fd, sx, sy):
    if fd == 9:
        return move(fx, fy, 1, sx, sy)
    nx = fx + dx[fd]
    ny = fy + dy[fd]
    if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
        return move(fx, fy, fd + 1, sx, sy)
    return nx, ny, fd


def sharkattack(sx, sy, fish, arr, pt):
    global ans
    
    if not (0 <= sx < 4 and 0 <= sy < 4) or not fish[arr[sx][sy]][2]:
        ans = max(ans, pt)
        return
    
    tempfish = deepcopy(fish)
    temparr = deepcopy(arr)
    
    fidx = temparr[sx][sy]
    sd = tempfish[fidx][2]
    tempfish[fidx][2] = 0
    
    for i in range(1, 17):
        if not tempfish[i][2]:
            continue
        fx = tempfish[i][0]
        fy = tempfish[i][1]
        fd = tempfish[i][2]
        nx, ny, fd = move(fx, fy, fd, sx, sy)

        fi= temparr[nx][ny]
        temparr[fx][fy], temparr[nx][ny] = temparr[nx][ny], temparr[fx][fy]
        tempfish[i] = [nx, ny, fd]
        tempfish[fi] = [fx, fy, tempfish[fi][2]]
        
    for j in range(1, 4):
        nsx = sx + j * dx[sd]
        nsy = sy + j * dy[sd]
        sharkattack(nsx, nsy, tempfish, temparr, pt + fidx)


arr = []
fish = [0 for i in range(17)]
for i in range(4):
    I = list(map(int, input().split()))
    arr.append([I[0], I[2], I[4], I[6]])
    for j in range(4):
        fish[I[2 * j]] = [i, j, I[2 * j + 1]]
        
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
ans = 0

sharkattack(0, 0, fish, arr, 0)

print(ans)