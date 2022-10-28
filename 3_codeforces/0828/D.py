def recur(i, j, d):
    global s
    y = i + d[0]
    x = j + d[1]
    
    if not 0 <= y < n or not 0 <= x < m:
        return
    
    s += arr[y][x]
    recur(y, x, d)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(n)]
    
    D1 = [(1, -1), (-1, 1)]
    D2 = [(1, 1), (-1, -1)]
    diag_1 = [-1]*(n + m)
    diag_2 = [-1]*(n + m)

    for i in range(n):
        for j in range(m):
            if diag_1[i + j] >= 0:
                continue
            
            s = arr[i][j]
            for d in D1:
                recur(i, j, d)
            diag_1[i + j] = s
    
    for i in range(n):
        for j in range(m):
            if diag_2[j - i + n] >= 0:
                continue
            
            s = arr[i][j]
            for d in D2:
                recur(i, j, d)
            diag_2[j - i + n] = s
    
    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(ans, diag_1[i + j] + diag_2[j - i + n] - arr[i][j])
    
    print(ans)
