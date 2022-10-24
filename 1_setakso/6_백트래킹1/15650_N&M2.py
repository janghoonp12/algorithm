def recur(cur, start):
    if cur == M:
        print(*arr)
        return
    
    for i in range(start, N):
        arr[cur] = i + 1
        recur(cur + 1, i + 1)


N, M = map(int, input().split())
arr = [0 for i in range(M)]

recur(0, 0)