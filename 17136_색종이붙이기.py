def check(x, y, n):
    if x + n > 10 or y + n > 10:
        return False
    for i in range(n):
        for j in range(n):
            if not arr[x + i][y + j] or visited[x + i][y + j]:
                return False
    return True


def cover(x, y, n):
    for i in range(n):
        for j in range(n):
            visited[x + i][y + j] = True


def uncover(x, y, n):
    for i in range(n):
        for j in range(n):
            visited[x + i][y + j] = False


def recur(x, y, cnt):
    global ans
    if cnt >= ans:
        return
    
    if max(paper_cnt) > 5:
        return

    if y == 10:
        recur(x + 1, 0, cnt)
        return

    if x == 10:
        ans = min(ans, cnt)
        return
    
    if not arr[x][y] or visited[x][y]:
        recur(x, y + 1, cnt)
    else:
        for i in range(5):
            if not check(x, y, 5 - i):
                continue
            
            cover(x, y, 5 - i)
            paper_cnt[i] += 1
            recur(x, y + 1, cnt + 1)
            uncover(x, y, 5 - i)
            paper_cnt[i] -= 1


arr = [list(map(int, input().split())) for i in range(10)]
visited = [[False for i in range(10)] for j in range(10)]
paper_cnt = [0 for i in range(5)]
ans = float('INF')

recur(0, 0, 0)

if ans == float('INF'):
    print(-1)
else:
    print(ans)