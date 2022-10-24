from collections import deque

def pour(cur, i, j):
    nxt = [cur[k] for k in range(3)]
    if nxt[i] > V[j] - nxt[j]:
        nxt[i] -= V[j] - nxt[j]
        nxt[j] = V[j]
    else:
        nxt[j] += nxt[i]
        nxt[i] = 0
    return tuple(nxt)

V = list(map(int, input().split()))
que = deque()
v = [[1, 2], [0, 2], [0, 1]]
visited = []

que.append((0, 0, V[2]))
visited.append((0, 0, V[2]))
while len(que) > 0:
    cur = que[0]
    que.popleft()
    
    for i in range(3):
        for j in v[i]:
            nxt = pour(cur, i, j)
            
            if nxt in visited:
                continue
            
            que.append(nxt)
            visited.append(nxt)

ans = set()
for i in visited:
    if not i[0]:
        ans.add(i[2])
        
ans = sorted(list(ans))

print(*ans)