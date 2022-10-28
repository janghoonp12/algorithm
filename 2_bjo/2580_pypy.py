def recur(x, y):
    if y == 9:
        x += 1
        y = 0
    if x == 9:
        for i in arr:
            print(*i)
        quit()

    if arr[x][y] != 0:
        recur(x, y + 1)
    else:
        for i in range(1, 10):
            if i in arr[x] or i in arr_2[y] or i in arr_3[3 * (x // 3) + y // 3]:
                continue
            arr[x][y] = i
            arr_2[y][x] = i
            arr_3[3 * (x // 3) + y // 3][3 * (x % 3) + y % 3] = i
            recur(x, y + 1)
        arr[x][y] = 0
        arr_2[y][x] = 0
        arr_3[3 * (x // 3) + y // 3][3 * (x % 3) + y % 3] = 0


arr = [list(map(int, input().split())) for i in range(9)]
arr_2 = [[0] * 9 for i in range(9)]
arr_3 = [[0] * 9 for i in range(9)]
for i in range(9):
    for j in range(9):
        arr_2[i][j] = arr[j][i]
        arr_3[i][j] = arr[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3]

recur(0, 0)
