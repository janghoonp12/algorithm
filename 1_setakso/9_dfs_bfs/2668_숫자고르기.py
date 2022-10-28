def dfs(n):
    global ans
    
    if visited[n]:
        return
    
    if n in arr:
        if n == arr[0]:
            ans += arr
            for i in arr:
                visited[i] = True
        return
    
    arr.append(n)
    dfs(v[n])


N = int(input())
v = [0] + [int(input()) for i in range(N)]
visited = [False for i in range(N + 1)]
ans = []

for i in range(1, N + 1):
    arr = []
    dfs(i)

ans.sort()

print(len(ans))
for i in ans:
    print(i)