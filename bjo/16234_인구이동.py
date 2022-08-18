from sys import stdin
I = stdin.readline

def move(N, L, R, Arr):
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    stack = []
    area = 1
    visited = [[0]*N for _ in range(N)]
    values = [0]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = area
                stack.append((i, j))
                stack_sum = Arr[i][j]
                stack_count = 1
                
                while stack:
                    i, j = stack[-1]
                    for (di, dj) in delta:
                        x, y = i+di, j+dj
                        if 0 <= x < N and 0 <= y < N and visited[x][y] == 0:
                            diff = abs(Arr[x][y] - Arr[i][j])
                            if L <= diff <= R:
                                visited[x][y] = area
                                stack.append((x, y))
                                stack_sum += Arr[x][y]
                                stack_count += 1
                                break
                    else:
                        stack.pop()
                
                values.append(stack_sum // stack_count)
                area += 1

    A = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            A[i][j] = values[visited[i][j]]
    
    return A

N, L, R = map(int, I().split())
Arr = [list(map(int, I().split())) for _ in range(N)]
  
ans = 0
while True:
    ans += 1
    A = move(N, L, R, Arr)
    
    if A == Arr:
        ans -= 1
        break
    else:
        Arr = A

print(ans)