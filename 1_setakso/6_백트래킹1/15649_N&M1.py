def recur(cur):
    if cur == M:
        print(*arr)
        return
    
    for i in range(N):
        if visited[i]:
            continue
        
        arr[cur] = i + 1
        visited[i] = True
        recur(cur + 1)
        visited[i] = False


N, M = map(int, input().split())
arr = [0 for i in range(M)]
visited = [False for i in range(N)]

recur(0)