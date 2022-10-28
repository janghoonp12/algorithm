from collections import deque

def bfs(N, M):
    queue = deque()
    queue.append(N)
    visited = [0] * 1000001
    visited[N] = 1
    while queue:
        n = queue.popleft()
        for i in (n + 1, n - 1, n * 2, n - 10):
            if i < 1 or i > 10**6 or visited[i]:
                continue
            if i == M:
                return visited[n]
            queue.append(i)
            visited[i] = visited[n] + 1



T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    ans = bfs(N, M)
    print(f'#{t}', ans)