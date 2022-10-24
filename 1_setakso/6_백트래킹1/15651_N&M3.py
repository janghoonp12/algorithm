def recur(cur):
    if cur == M:
        print(*arr)
        return
    
    for i in range(N):
        arr[cur] = i + 1
        recur(cur + 1)


N, M = map(int, input().split())
arr = [0 for i in range(M)]

recur(0)