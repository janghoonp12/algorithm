N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
firstplace = [0 for i in range(N)]
lastplace = [0 for i in range(N)]
sub_sum = [0 for i in range(N)]
sum_arr = [max(0, sum(arr[i])) for i in range(N)]

for i in range(N):
    prefix = 0
    suffix = 0
    m = 0
    for j in range(M):
        prefix += arr[i][j]
        suffix += arr[i][M - j - 1]
        m = min(m, prefix)
        
        firstplace[i] = max(firstplace[i], suffix)
        lastplace[i] = max(lastplace[i], prefix)
        sub_sum[i] = max(sub_sum[i], prefix - m)

ans = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        temp = firstplace[i] + lastplace[j]
        for k in range(N):
            if k == i or k == j:
                continue
            temp += sum_arr[k]
        ans = max(ans, temp)

ans = max(ans, max(sub_sum))
print(ans)