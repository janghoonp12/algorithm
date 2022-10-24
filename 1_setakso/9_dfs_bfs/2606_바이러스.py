def dfs(cur):
    global cnt

    visited[cur] = True
    cnt += 1

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        dfs(nxt)


N = int(input())
M = int(input())
v = [[] for i in range(N + 1)]
visited = [False] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

cnt = 0
dfs(1)

print(cnt - 1)