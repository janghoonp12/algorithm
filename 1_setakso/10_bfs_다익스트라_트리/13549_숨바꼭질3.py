import heapq


N, K = map(int, input().split())
M = max(N + 1, 2 * K + 1)
dist = [float('INF') for i in range(M)]
visited = [False for i in range(M)]
mul = [2, 1, 1]
add = [0, 1, -1]
dd = [0, 1, 1]

pq = []
heapq.heappush(pq, [0, N])
dist[N] = 0
while len(pq) > 0:
    cur = heapq.heappop(pq)
    
    d = cur[0]
    idx = cur[1]
    
    if visited[idx]:
        continue
    
    visited[idx] = True
    
    for i in range(3):
        nxt = mul[i] * idx + add[i]
        if not 0 <= nxt < M:
            continue
        nd = dist[idx] + dd[i]
        
        if dist[nxt] > nd:
            dist[nxt] = nd
            heapq.heappush(pq, [nd, nxt])

print(dist[K])