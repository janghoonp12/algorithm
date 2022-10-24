N = int(input())
arr_x = set()
arr_y = set()
arr = []

for i in range(N):
    x, y = map(int, input().split())
    arr_x.add(x)
    arr_y.add(y)
    arr.append((x, y))

arr_x = list(arr_x)
arr_y = list(arr_y)
ans = [float('inf')] * N
dist = [0] * N

for i in arr_x:
    for j in arr_y:
        for k in range(N):
            dist[k] = abs(arr[k][0] - i) + abs(arr[k][1] - j)
        dist.sort()
        for k in range(N):
            ans[k] = min(ans[k], sum(dist[:k + 1]))

print(*ans)