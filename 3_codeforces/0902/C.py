t = int(input())
for _ in range(t):
    n = int(input())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    
    ans = True
    
    check = [False]*n
    count = 0
    for i in range(n):
        if arr_a[i] > arr_b[i]:
            ans = False
            break
        elif arr_a[i] == arr_b[i]:
            count += 1
            check[i] = True
        elif arr_b[i] > arr_b[(i + 1) % n] + 1:
            ans = False
            break
        else:
            arr_a[i] = min(arr_b[i], arr_a[(i + 1) % n] + 1)
            
    while ans:
        change = 0
        for i in range(n):
            if check[i]:
                continue
            elif arr_a[i] == arr_b[i]:
                count += 1
                check[i] = True
            else:
                arr_a[i] = min(arr_b[i], arr_a[(i + 1) % n] + 1)
                change += 1
        
        if count == n:
            break
        
        elif not change:
            ans = False
    
    if ans:
        print('YES')
    else:
        print('NO')