import heapq


N, M, K, X = map(int, input().split())
v = [[] for i in range(N + 1)]
dist = [float('INF') for i in range(N + 1)]
visited = [False for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    
    v[a].append(b)

pq = []
heapq.heappush(pq, [0, X])
dist[X] = 0
while len(pq) > 0:
    cur = heapq.heappop(pq)
    
    d = cur[0]
    idx = cur[1]
    
    if visited[idx]:
        continue
    
    visited[idx] = True
    
    for nxt in v[idx]:
        nd = dist[idx] + 1
        
        if dist[nxt] > nd:
            dist[nxt] = nd
            heapq.heappush(pq, [nd, nxt])

ans = []
for i in range(1, N + 1):
    if dist[i] == K:
        ans.append(i)

if ans:
    for i in ans:
        print(i)
else:
    print(-1)