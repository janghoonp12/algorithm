import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline

def dfs(cur, prv):
    for nxt in v[cur]:
        if nxt == prv:
            continue
        
        dfs(nxt, cur)
        sz[cur] += sz[nxt]
        

N, R, Q = map(int, input().split())
v = [[] for i in range(N + 1)]
sz = [1 for i in range(N + 1)]

for i in range(N - 1):
    a, b = map(int, input().split())
    
    v[a].append(b)
    v[b].append(a)


dfs(R, 0)

for i in range(Q):
    U = int(input())
    print(sz[U])