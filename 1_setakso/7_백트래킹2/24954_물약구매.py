def recur(cur, cost):
    global ans
    
    if cur == N:
        ans = min(ans, cost)
        return
    
    for i in range(N):
        if visited[i]:
            continue
        
        visited[i] = True
        for info in sale_info[i]:
            price[info[0] - 1] -= info[1]
        recur(cur + 1, cost + max(1, price[i]))
        visited[i] = False
        for info in sale_info[i]:
            price[info[0] - 1] += info[1]


N = int(input())
price = list(map(int, input().split()))
sale = [0] * N
sale_info = [[] for i in range(N)]
for i in range(N):
    sale[i] = p = int(input())
    for j in range(p):
        sale_info[i].append(tuple(map(int, input().split())))

visited = [False] * N
ans = sum(price)

recur(0, 0)

print(ans)