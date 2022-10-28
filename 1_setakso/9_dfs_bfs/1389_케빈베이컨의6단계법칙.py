from collections import deque


N, M = map(int, input().split())
v = [[] for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

kb = [[0 for i in range(N + 1)] for j in range(N + 1)]

for i in range(1, N + 1):
    que = deque()
    visited = [False for i in range(N + 1)]
    
    que.append(i)
    visited[i] = True
    while len(que) > 0:
        cur = que[0]
        que.popleft()
        
        for nxt in v[cur]:
            if visited[nxt]:
                continue
            
            que.append(nxt)
            visited[nxt] = True
            kb[i][nxt] = kb[i][cur] + 1

ans = 0
mkb = float('inf')
for i in range(1, N + 1):
    if sum(kb[i]) < mkb:
        ans = i
        mkb = sum(kb[i])

print(ans)