import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline

def dfs(cur, pvs):
    for nxt in v[cur]:
        if nxt == pvs:
            continue
        
        par[nxt] = cur
        depth[nxt] = depth[cur] + 1
        dfs(nxt, cur)


N = int(input())
v = [[] for i in range(N + 1)]
par = [-1 for i in range(N + 1)]
depth = [0 for i in range(N + 1)]

for i in range(N - 1):
    a, b = map(int, input().split())
    
    v[a].append(b)
    v[b].append(a)

dfs(1, 0)

M = int(input())
for i in range(M):
    a, b = map(int, input().split())
    while True:
        if depth[a] > depth[b]:
            a = par[a]
        elif depth[b] > depth[a]:
            b = par[b]
        elif a != b:
            a = par[a]
            b = par[b]
        else:
            print(a)
            break