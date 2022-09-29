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
        check[cur] = i
        recur(cur + 1, p * arr[cur][i] / 100)
        visited[i] = False


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    check = [0] * N
    ans = 0
    visited = [False] * N

    recur(0, 1)
    
    print(f'#{t} {(ans * 100):.6f}')
