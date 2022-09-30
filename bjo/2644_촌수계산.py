from collections import deque


n = int(input())
a, b = map(int, input().split())
m = int(input())
v = [[] for i in range(n + 1)]
visited = [False for i in range(n + 1)]
dist = [0 for i in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    v[x].append(y)
    v[y].append(x)

que = deque()

que.append(a)
visited[a] = True

while len(que) > 0:
    cur = que[0]
    que.popleft()
        
    for nxt in v[cur]:
        if visited[nxt]:
            continue

        que.append(nxt)
        visited[nxt] = True
        dist[nxt] = dist[cur] + 1

ans = dist[b] if dist[b] else -1
print(ans)