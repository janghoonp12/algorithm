import heapq

V, E = map(int, input().split())
v = [[] for i in range(V + 1)]
dist = [float('INF') for i in range(V + 1)]
visited = [False for i in range(V + 1)]
K = int(input())
for i in range(E):
    a, b, c = map(int, input().split())
    
    v[a].append([b, c])

pq = []
heapq.heappush(pq, [0, K])
dist[K] = 0
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

for i in range(1, V + 1):
    if dist[i] == float('INF'):
        print('INF')
    else:
        print(dist[i])