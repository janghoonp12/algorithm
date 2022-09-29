def dfs(cur):
    visited[cur] = True

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        dfs(nxt)


N, M = map(int, input().split())
v = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

cnt = 0
for i in range(1, N + 1):
    if visited[i]:
        continue
    
    cnt += 1
    dfs(i)

print(cnt)