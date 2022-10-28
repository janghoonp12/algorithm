t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [['.'] * (m + 2)] + [['.'] + list(input()) + ['.'] for i in range(n)] + [['.'] * (m + 2)]
    check = [[0]*m for i in range(n)]
    D = [(-1, -1), (-1, 0), (-1, 1), (-1, 2), (0, -1), (0, 2), (1, -1), (1, 2), (2, -1), (2, 0), (2, 1), (2, 2)]
    
    count = 0
    star = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr[i][j] == '*':
                count += 1
                
    for i in range(1, n):
        for j in range(1, m):
            s = 0
            d = 0
            for k in range(4):
                if arr[i + k // 2][j + k % 2] == '*':
                    s += 1
                else:
                    keep = k
            if s == 3:
                for k in range(12):
                    if keep == 0 and k == 0:
                        continue
                    elif keep == 1 and k == 3:
                        continue
                    elif keep == 2 and k == 8:
                        continue
                    elif keep == 3 and k == 11:
                        continue
                    
                    if arr[i + D[k][0]][j + D[k][1]] == '*':
                        break
                else:
                    star += 3

    if count == star:
        print('YES')
    else:
        print('NO')