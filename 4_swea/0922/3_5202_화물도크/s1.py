T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    arr.sort(key=lambda x: x[1])
    ans = e = 0
    for i in arr:
        if i[0] >= e:
            ans += 1
            e = i[1]
    print(f'#{t}', ans)