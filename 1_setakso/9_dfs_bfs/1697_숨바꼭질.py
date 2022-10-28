from collections import deque


N, K = map(int, input().split())
visited = [False for i in range(200010)]
dist = [0 for i in range(200010)]

mul = [1, 1, 2]
add = [-1, 1, 0]

que = deque()

que.append(N)
visited[N] = True
while len(que) > 0:
    cur = que[0]
    que.popleft()
    
    if cur == K:
        break
    
    for i in range(3):
        nxt = mul[i] * cur + add[i]
        if not (0 <= nxt < 200010) or visited[nxt]:
            continue
        
        que.append(nxt)
        visited[nxt] = True
        dist[nxt] = dist[cur] + 1

print(dist[K])