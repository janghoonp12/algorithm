t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    arr = [[0]*1001 for i in range(1001)]
    for i in range(n):
        h, w = map(int, input().split())
        arr[h][w] += 1
    
    for i in range(1, 1001):
        for j in range(1, 1001):
            arr[i][j] = arr[i][j] * i * j
    
    prefix = [[0]*1001 for i in range(1001)]
    
    for i in range(1, 1001):
        for j in range(1, 1001):
            prefix[i][j] = arr[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
    
    for i in range(q):
        hs, ws, hb, wb = map(int, input().split())
        print(prefix[hb-1][wb-1] - prefix[hb-1][ws]- prefix[hs][wb - 1]+ prefix[hs][ws])