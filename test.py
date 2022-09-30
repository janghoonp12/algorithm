def dfs(cur):
    print(cur)
    global check
    if cur == temp:
        check = True
        return
    
    if visited[v[cur]]:
        return
    
    dfs(v[cur])
    if check:
        visited[cur] = True
        numbers.append(cur)


N = int(input())
v = [0] + [int(input()) for i in range(N)]
visited = [False for i in range(N + 1)]

numbers = []
for i in range(1, N + 1):
    if visited[i]:
        continue

    temp = i
    visited[i] = True
    check = False
    dfs(v[i])
    if check:
        numbers.append(i)

print(numbers)