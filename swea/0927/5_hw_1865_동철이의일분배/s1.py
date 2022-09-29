def recur(cur, p):
    global ans

    if p <= ans:
        return
    
    if cur == N:
        ans = p
        return
    
    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        recur(cur + 1, p * arr[cur][i] / 100)
        visited[i] = False


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    
    visited = [False] * N
    ans = 1
    for i in range(N):
        temp = 0
        for j in range(N):
            if visited[j]:
                continue
            visited[j] = True
            temp = max(temp, arr[i][j])
        ans *= temp / 100

    visited = [False] * N
    recur(0, 1)
    
    print(f'#{t} {(ans * 100):.6f}')