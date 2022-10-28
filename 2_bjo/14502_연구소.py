import copy
from sys import stdin
I = stdin.readline

def safty(arr):
    lab = copy.deepcopy(map)
    for i, j in arr:
        lab[i][j] = 1
    queue = virus[:]
    
    while queue:
        i, j = queue.pop(0)
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            y = i + di
            x = j + dj
            if not 0 <= y < N or not 0 <= x < M or lab[y][x]:
                continue
            lab[y][x] = 2
            queue.append((y, x))
    
    count = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 9
                count += 1
    
    return count


def recur(cur, start):
    global ans
    if cur == 3:
        ans = max(ans, safty(arr))
        return
        
    for i in range(start, len(location)):
        arr[cur] = location[i]
        recur(cur + 1, i + 1)


N, M = map(int, I().split())
map = [list(map(int, I().split())) for i in range(N)]

location = []
virus = []
for i in range(N):
    for j in range(M):
        if map[i][j] == 0:
            location.append((i, j))
        elif map[i][j] == 2:
            virus.append((i, j))
            
arr = [0] * 3
ans = 0

recur(0, 0)

print(ans)