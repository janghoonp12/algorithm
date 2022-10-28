def recur(cur):
    global ans
    if cur >= 2:
        if ineq[cur - 2] == '<' and arr[cur - 2] > arr[cur - 1]:
            return
        if ineq[cur - 2] == '>' and arr[cur - 2] < arr[cur - 1]:
            return
    
    if cur == k + 1:
        ans.append(arr[:])
        return
    
    for i in range(10):
        if visited[i]:
            continue
        
        arr[cur] = i
        visited[i] = True
        recur(cur + 1)
        visited[i] = False


k = int(input())
ineq = list(input().split())
visited = [False for i in range(10)]
arr = [0 for i in range(k + 1)]
ans = []

recur(0)

for i in (-1, 0):
    for j in range(k + 1):
        print(ans[i][j], end = '')
    print()