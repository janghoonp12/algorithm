T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr_N = sorted(list(map(int, input().split())))
    arr_M = list(map(int, input().split()))

    ans = 0
    for i in arr_M:
        s = 0
        e = N - 1
        m = (s + e) // 2
        p = True
        if arr_N[m] < i:
            p = False
        while s <= e:
            m = (s + e) // 2
            if arr_N[m] < i:
                if p:
                    break
                s = m + 1
                p = True
            elif arr_N[m] > i:
                if not p:
                    break
                e = m - 1
                p = False
            else:
                ans += 1
                break

    print(f'#{t}', ans)