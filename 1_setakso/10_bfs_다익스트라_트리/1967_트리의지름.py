import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline

def dfs(cur, pvs):
    for i in v[cur]:
        nxt = i[0]
        nd = i[1]
        if nxt == pvs:
            continue
        
        dist[nxt] = dist[cur] + nd
        dfs(nxt, cur)


n = int(input())
v = [[] for i in range(n + 1)]
dist = [0 for i in range(n + 1)]

for i in range(n - 1):
    a, b, c = map(int, input().split())
    
    v[a].append([b, c])
    v[b].append([a, c])

dfs(1, 0)

m = max(dist)
e = dist.index(m)
dist[e] = 0

dfs(e, 0)

print(max(dist))