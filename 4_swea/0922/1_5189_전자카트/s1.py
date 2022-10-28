def recur(cur, total, room):
    global ans 

    if cur == N - 1:
        ans = min(ans, total + arr[room][0])
        return

    for i in range(1, N):
        if visited[i]:
            continue
        
        visited[i] = True
        recur(cur + 1, total + arr[room][i], i)
        visited[i] = False


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    visited = [False] * N
    ans = 100 * N

    recur(0, 0, 0)

    print(f'#{t}', ans)