import copy
from sys import stdin
I = stdin.readline

def virus(arr):
    queue = arr[:]
    la = copy.deepcopy(lab)
    for i, j in queue:
        la[i][j] = 1
    
    while queue:
        i, j = queue.pop(0)
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            y = i + di
            x = j + dj
            if not 0 <= y < N or not 0 <= x < N or la[y][x]:
                continue
            else:
                queue.append((y, x))
                la[y][x] = la[i][j] + 1
    return la


def recur(cur, start):
    global possible, ans
    
    if cur == M:
        final_lab = virus(arr)
        num = 0
        zero_count = 0
        for i in range(N):
            for j in range(N):
                num = max(num, final_lab[i][j])
                if final_lab[i][j] == 0:
                    zero_count += 1
        if not zero_count:
            possible = True 
            ans = min(ans, num)
        return
        
    for i in range(start, len(location)):
        
        arr[cur] = location[i]
        recur(cur + 1, i + 1)



N, M = map(int, I().split())
map = [list(map(int, I().split())) for i in range(N)]

lab = [[0] * N for i in range(N)]
location = []
for i in range(N):
    for j in range(N):
        if map[i][j] == 2:
            location.append((i, j))
        if map[i][j] == 1:
            lab[i][j] = -1

arr = [0] * M

ans = 5000
possible = False

recur(0, 0)

if possible:
    print(ans - 1)
else:
    print(-1)