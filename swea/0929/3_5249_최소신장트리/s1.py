def check_cycle(n):
    if v[n] == n:
        return n
    
    return check_cycle(v[n])


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(E)]
    arr.sort(key = lambda x : x[2])
    v = [i for i in range(V + 1)]
    cnt = ans = 0
    for i in range(E):
        if check_cycle(arr[i][0]) == check_cycle(arr[i][1]):
            continue
        
        cnt += 1
        ans += arr[i][2]
        v[check_cycle(arr[i][1])] = check_cycle(arr[i][0])
        if cnt == V:
            break

    print(f'#{t}', ans)