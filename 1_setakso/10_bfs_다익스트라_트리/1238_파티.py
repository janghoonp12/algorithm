import heapq


def dijkstra(s, v):
    dist = [float('INF') for i in range(N + 1)]
    visited = [False for i in range(N + 1)]
    pq = []
    heapq.heappush(pq, [0, s])
    dist[s] = 0
    while len(pq) > 0:
        cur = heapq.heappop(pq)

        d = cur[0]
        idx = cur[1]

        if visited[idx]:
            continue
        
        visited[idx] = True

        for i in v[idx]:
            nxt = i[0]
            nd = dist[idx] + i[1]

            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(pq, [nd, nxt])
    
    return dist

N, M, X = map(int, input().split())
v1 = [[] for i in range(N + 1)]
v2 = [[] for i in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    v1[b].append([a, c])
    v2[a].append([b, c])

dist1 = dijkstra(X, v1)
dist2 = dijkstra(X, v2)
ans = 0
for i in range(1, N + 1):
    ans = max(ans, dist1[i] + dist2[i])

print(ans)