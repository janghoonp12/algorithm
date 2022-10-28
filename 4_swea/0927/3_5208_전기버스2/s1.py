def recur(cur, battery, count):
    global ans

    if battery < 0 or count >= ans:
        return

    if cur == arr[0]:
        ans = min(ans, count)
        return
    
    recur(cur + 1, battery - 1, count)
    recur(cur + 1, arr[cur] - 1, count + 1)


T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    ans = arr[0]

    recur(2, arr[1] - 1, 0)
    
    print(f'#{t}', ans)