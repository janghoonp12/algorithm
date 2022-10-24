def recur(cur, start):
    global ans
    
    if cur == n:
        count = 0
        for i in Q_arr:
            for j in i:
                if j not in arr:
                    break
            else:
                count += 1
        ans = max(ans, count)
        return
    
    for i in range(start, 2 * n + 1):
        arr[cur] = i
        recur(cur + 1, i + 1)


n, m, k = list(map(int, input().split()))
Q_arr = [list(map(int, input().split())) for i in range(m)]

arr = [0] * (n)
ans = 0

recur(0, 1)

print(ans)