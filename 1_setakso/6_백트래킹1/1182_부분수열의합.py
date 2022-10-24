def recur(cur, start):
    global ans
    
    if cur and sum(arr[:cur]) == S:
        ans += 1
    
    if cur == N:
        return
    
    for i in range(start, N):
        arr[cur] = N_arr[i]
        recur(cur + 1, i + 1)


N, S = map(int, input().split())
N_arr = list(map(int, input().split()))
arr = [False for i in range(N)]
ans = 0

recur(0, 0)

print(ans)
