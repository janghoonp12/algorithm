def check(i, j, d):
    y, x = i + d[0], j + d[1]
    if 0 <= x < M and 0 <= y < N and office[y][x] != 6:
        arr[y][x] += 1
        check(y, x, d)
    return

def uncheck(i, j, d):
    y, x = i + d[0], j + d[1]
    if 0 <= x < M and 0 <= y < N and office[y][x] != 6:
        arr[y][x] -= 1
        uncheck(y, x, d)
    return

def recur(cur):
    global ans
    
    if cur == len(cctv):
        s = 0
        for i in range(N):
            for j in range(M):
                if not arr[i][j]:
                    s += 1
        ans = min(ans, s)
        return
    
    i, j, c = cctv[cur]
    arr[i][j] += 1
    if c == 5:
        for d in D:
            check(i, j, d)
        recur(cur + 1)
        for d in D:
            uncheck(i, j, d)
            
    elif c == 4:
        for k in range(4):
            for d in range(4):
                if d == k:
                    continue
                check(i, j, D[d])
            recur(cur + 1)
            for d in range(4):
                if d == k:
                    continue
                uncheck(i, j, D[d])
                
    elif c == 3:
        for k in range(4):
            for d in range(4):
                if d == k//2 or d == 2 + k % 2:
                    continue
                check(i, j, D[d])
            recur(cur + 1)
            for d in range(4):
                if d == k//2 or d == 2 + k % 2:
                    continue
                uncheck(i, j, D[d])
        
    elif c == 2:
        for k in range(2):
            for d in D[2 * k : 2 * (k + 1)]:
                check(i, j , d)
            recur(cur + 1)
            for d in D[2 * k : 2 * (k + 1)]:
                uncheck(i, j , d)
                
    else:
        for d in D:
            check(i, j ,d)
            recur(cur + 1)
            uncheck(i, j, d)

N, M = map(int, input().split())
office = [list(map(int, input().split())) for i in range(N)]
cctv = []
arr = [[0]*M for i in range(N)]
D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(N):
    for j in range(M):
        if office[i][j] not in (0, 6):
            cctv.append((i, j, office[i][j]))
        elif office[i][j] == 6:
            arr[i][j] = 6

ans = N * M
recur(0)

print(ans)