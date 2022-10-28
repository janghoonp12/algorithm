def dfs(cur, prv):
    global idx
    if cur == -1:
        return
    depth[cur] = depth[prv] + 1
    dfs(v[cur][0], cur)
    arr[cur] = idx
    idx += 1
    dfs(v[cur][1], cur)


N = int(input())
v = [0 for i in range(N + 1)]
depth = [0 for i in range(N + 1)]
check = [0 for i in range(N + 2)]
for i in range(N):
    a, b, c = map(int, input().split())
    v[a] = [b, c]
    check[b] = a
    check[c] = a

root = check[1:].index(0) + 1

idx = 1
arr = [0 for i in range(N + 1)]

dfs(root, 0)

M = max(depth)
depth_list = [[] for i in range(M + 1)]

for i in range(N + 1):
    depth_list[depth[i]].append(i)

ans = [0, 0]
for i in range(1, M + 1):
    temp = [arr[depth_list[i][j]] for j in range(len(depth_list[i]))]
    d = max(temp) - min(temp) + 1
    if d > ans[1]:
        ans[1] = d
        ans[0] = i

print(*ans)