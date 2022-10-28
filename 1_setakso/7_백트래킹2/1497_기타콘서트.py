def recur(cur, count):
    global playable, ans
    
    if cur == N:
        num = 0
        for i in arr:
            if i:
                num += 1
        if num > playable:
            playable = num
            ans = count
        elif num == playable:
            ans = min(ans, count)
        return
    
    
    for i in range(M):
        if S_arr[cur][i] == 'Y':
            arr[i] += 1
    recur(cur + 1, count + 1)
    for i in range(M):
        if S_arr[cur][i] == 'Y':
            arr[i] -= 1
    
    recur(cur + 1, count)


N, M = map(int, input().split())
S_arr = []

for i in range(N):
    g, s = input().split()
    S_arr.append(s)
arr = [0] * M
playable = 0
ans = N

recur(0, 0)

if playable == 0:
    print(-1)
else:
    print(ans)