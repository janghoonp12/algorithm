def recur(cur):
    global ans

    if cur == 5:
        ans = max(ans, sum(arr))
        return
    
    for i in range(len(at_least)):
        if visited[i]:
            continue

        arr[cur] = at_least[i][cur]
        visited[i] = True
        recur(cur + 1)
        visited[i] = False


n = int(input())
status = [list(map(int, input().split())) for i in range(n)]
at_least = []
for i in range(5):
    if not status:
        break
    status.sort(key=lambda x : x[i])
    for j in range(5):
        if not status:
            break
        at_least.append(status.pop())
visited = [False for i in range(n)]
arr = [0]*5
ans = 0

recur(0)

print(ans)