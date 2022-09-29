def dfs(cur):
    visited[cur] = True
    for nxt in v[cur]:
        if visited[nxt]:
            continue

        dfs(nxt)


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    v = [[] for i in range(N + 1)]
    visited = [False] * (N + 1)
    
    for i in range(M):
        v[arr[2 * i]].append(arr[2 * i + 1])
        v[arr[2 * i + 1]].append(arr[2 * i])

    
    cnt = 0
    for i in range(1, N + 1):
        if visited[i]:
            continue

        cnt += 1
        dfs(i)
    
    print(f'#{t}', cnt)