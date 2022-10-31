def available_left(x, y):
    if not (0 <= x < N and 0 <= y < N):
        return True
    if bishop[x][y]:
        return False
    return available_left(x - 1, y - 1)


def available_right(x, y):
    if not (0 <= x < N and 0 <= y < N):
        return True
    if bishop[x][y]:
        return False
    return available_right(x - 1, y + 1)


def recur(cur, cnt, type):
    if cur == M[type]:
        cnt_ans[type] = max(cnt_ans[type], cnt)
        return
    
    x, y = possible[type][cur]
    if not available_left(x, y) or not available_right(x, y):
        recur(cur + 1, cnt, type)
        return
    
    bishop[x][y] = True
    recur(cur + 1, cnt + 1, type)
    bishop[x][y] = False
    recur(cur + 1, cnt, type)


N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
even = []
odd = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            if (i + j) % 2:
                odd.append((i, j))
            else:
                even.append((i, j))

M = (len(even), len(odd))

bishop = [[False for i in range(N)] for j in range(N)]
cnt_ans = [0, 0]
possible = [even, odd]

recur(0, 0, 0)
recur(0, 0, 1)

ans = sum(cnt_ans)
print(ans)