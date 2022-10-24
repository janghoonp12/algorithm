T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr_w = sorted(list(map(int, input().split())))[::-1]
    arr_t = sorted(list(map(int, input().split())))[::-1]
    p1 = p2 = ans = 0
    while p1 < N and p2 < M:
        if arr_w[p1] > arr_t[p2]:
            p1 += 1
        else:
            ans += arr_w[p1]
            p1 += 1
            p2 += 1

    print(f'#{t}', ans)