import heapq


def dijkstra(s):
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
    

N, E = map(int, input().split())
v = [[] for i in range(N + 1)]
for i in range(E):
    a, b, c = map(int, input().split())
    
    v[a].append([b, c])
    v[b].append([a, c])
    
v1, v2 = map(int, input().split())

dist_1 = dijkstra(1)
dist_v = dijkstra(v1)[v2]
dist_N = dijkstra(N)

ans = min(dist_1[v1] + dist_v + dist_N[v2], dist_1[v2] + dist_v + dist_N[v1])
if ans == float('INF'):
    print(-1)
else:
    print(ans)