from collections import deque


def dfs(cur):
    visited[cur] = True
    ans_dfs.append(cur)
    
    for nxt in sorted(v[cur]):
        if visited[nxt]:
            continue

        dfs(nxt)


N, M, V = map(int, input().split())
v = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

visited = [False] * (N + 1)
ans_dfs = []

dfs(V)

visited = [False] * (N + 1)
ans_bfs = []

que = deque()
que.append(V)
visited[V] = True
ans_bfs.append(V)

while len(que) > 0:
    cur = que[0]
    que.popleft()

    for nxt in sorted(v[cur]):
        if visited[nxt]:
            continue

        que.append(nxt)
        visited[nxt] = True
        ans_bfs.append(nxt)


print(*ans_dfs)
print(*ans_bfs)