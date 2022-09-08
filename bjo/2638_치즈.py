def melt(hour):
    global ans

    queue = [(0, 0)]
    c = 0
    visited = [[0] * M for i in range(N)]

    while queue:
        i, j = queue.pop()
        for di, dj in D:
            y, x = i + di, j + dj
            if not 0 <= y < N or not 0 <= x < M or visited[y][x] == 2:
                continue
            elif cheese[y][x] == 0:
                queue.append((y, x))
                visited[y][x] += 2
            elif cheese[y][x] == 1:
                if visited[y][x] == 1:
                    cheese[y][x] = 0
                    c += 1
                visited[y][x] += 1
    
    if c == 0:
        print(hour)
        return
    else:
        ans = (hour + 1, c)
        melt(hour + 1)


N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for i in range(N)]
D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

melt(0)