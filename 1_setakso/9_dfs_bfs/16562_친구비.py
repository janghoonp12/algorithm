import sys
sys.setrecursionlimit(100010)

def dfs(cur):
    global fee

    fee = min(fee, A[cur])
    visited[cur] = True

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        dfs(nxt)


N, M, k = map(int, input().split())
A = [0] + list(map(int, input().split()))
v = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

m = max(A)
friend_fee = 0
for i in range(1, N + 1):
    if visited[i]:
        continue
    
    fee = m
    dfs(i)
    friend_fee += fee

ans = friend_fee if friend_fee <= k else 'Oh no'
print(ans)