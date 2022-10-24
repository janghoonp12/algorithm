T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    m = max(arr)
    cnt_1 = cnt_2 = 0
    
    for i in arr:
        cnt_1 += (m - i) % 2
        cnt_2 += (m - i) // 2
    
    day = 0
    while cnt_1:
        if day % 2:
            day += 1
            if cnt_2:
                cnt_2 -= 1
        else:
            day += 1
            cnt_1 -= 1
    
    while cnt_2:
        if day % 2:
            day += 1
            cnt_2 -= 1
        else:
            if cnt_2 == 1:
                day += 2
                cnt_2 -= 1
            else:
                day += 3
                cnt_2 -= 2
    
    print(f'#{t}', day)