def recur(i, j, s):
    global ans
    
    if i == N or j == N:
        return
    if i == j == N - 1:
        ans = min(ans, s)
        return
    
    recur(i + 1, j, s + arr[i + 1][j])
    recur(i, j + 1, s + arr[i][j + 1])


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) + [0] for i in range(N)] + [[0] * (N + 1)]
    ans = 20 * N
    recur(0, 0, arr[0][0])
    print(f'#{t}', ans)