def recur(cur):
    if cur == M:
        print(*arr)
        return
    
    for i in range(N):
        if visited[i]:
            continue
        
        arr[cur] = N_arr[i]
        visited[i] = True
        recur(cur + 1)
        visited[i] = False


N, M = map(int, input().split())
visited = [False for i in range(N)]
N_arr = list(map(int, input().split()))
N_arr.sort()
arr = [0 for i in range(M)]

recur(0)