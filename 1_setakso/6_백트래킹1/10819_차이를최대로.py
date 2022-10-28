def eq(arr):
    s = 0
    for i in range(N - 1):
        s += abs(arr[i] - arr[i + 1])
    return s

def recur(cur):
    global ans

    if cur == N:
        ans = max(ans, eq(arr))
        return

    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        arr[cur] = n_arr[i]
        recur(cur + 1)
        visited[i] = False


N = int(input())
n_arr = list(map(int, input().split()))
arr = [0 for i in range(N)]
visited = [False for i in range(N)]
ans = 0

recur(0)
print(ans)