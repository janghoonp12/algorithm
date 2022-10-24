def flood():
    queue = start_water[:]
    while queue:
        i, j = queue.pop(0)
        
        for di, dj in delta:
            y, x = i + di, j + dj
            if 0 <= y < R and 0 <= x < C:
                if not arr[y][x] and not water[y][x]:
                    water[y][x] = water[i][j] + 1
                    queue.append((y, x))

def run(si, sj):
    global ans
    
    queue = [(si, sj)]
    while queue:
        i, j = queue.pop(0)
        for di, dj in delta:
            y, x = i + di, j + dj
            if 0 <= y < R and 0 <= x < C:
                if y == ei and x == ej:
                    ans = arr[i][j]
                    return
                if (not water[y][x] or arr[i][j] + 1 < water[y][x]) and not arr[y][x]:
                    arr[y][x] = arr[i][j] + 1
                    queue.append((y, x))
    
        

R, C = map(int, input().split())
arr = [list(input()) for i in range(R)]
water = [[False] * C for i in range(R)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
start_water = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == '.':
            arr[i][j] = 0
        elif arr[i][j] == 'S':
            arr[i][j] = 1
            si, sj = i, j
        elif arr[i][j] == 'D':
            ei, ej = i, j
        elif arr[i][j] == '*':
            water[i][j] = 1
            start_water.append((i, j))
ans = 'KAKTUS'
flood()
run(si, sj)
print(ans)