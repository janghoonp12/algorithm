from collections import deque
from sys import stdin
input = stdin.readline


N = int(input())
S = '0' + input()
v = [[] for i in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    
    v[a].append(b)
    v[b].append(a)

visited = [False for i in range(N + 1)]

que = deque()

que.append(1)
visited[1] = True

ans = ''
M = S[1]
nxtque = que
while len(nxtque) > 0:
    ans += M
    que = nxtque
    nxtque = deque()
    M = 'a'
    while len(que) > 0:
        cur = que[0]
        que.popleft()

        for nxt in v[cur]:
            if visited[nxt] or S[nxt] < M:
                continue

            elif S[nxt] == M:
                nxtque.append(nxt)
                visited[nxt] = True

            elif S[nxt] > M:
                nxtque = deque()
                nxtque.append(nxt)
                visited[nxt] = True
                M = S[nxt]
        
print(ans)