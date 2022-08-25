# import sys
# sys.stdin = open('input.txt', 'r')

for _ in range(10):
    t = int(input())
    arr = [list(input()) for i in range(16)]
    
    b = False
    for i in range(16):
        if b:
            break
        for j in range(16):
            if arr[i][j] == '2':
                s = (i, j)
                b = True
                break

    visited = [[0]*16 for i in range(16)]
    queue = [s]
    ans = 0
    fin = False
    while queue:
        if fin:
            break

        i, j = queue.pop(0)
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x = i + di
            y = j + dj
            if not 0 <= x < 16 or not 0 <= y < 16:
                continue

            if arr[x][y] == '3':
                ans = 1
                fin = True
                break
            
            if not visited[x][y] and arr[x][y] == '0':
                visited[x][y] = 1
                queue.append((x, y))

    print(f'#{t} {ans}')
