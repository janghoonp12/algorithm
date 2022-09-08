def recur(cur, damage, hp, point, last_ppl):
    global ans
    
    if hp < 0:
        ans = max(ans, point - last_ppl)
        return
    elif cur == N:
        if hp == K:
            return
        else:
            ans = max(ans, point)
            return

    
    recur(cur + 1, damage + arr[cur][0], hp - damage - arr[cur][0], point + arr[cur][1], arr[cur][1])
    recur(cur + 1, damage, hp, point, last_ppl)

N, K = map(int, input().split())
Atk = tuple(map(int, input().split()))
Ppl = tuple(map(int, input().split()))

arr = [(Atk[i], Ppl[i]) for i in range(N)]
arr.sort()
ans = 0

recur(0, 0, K, 0, 0)

print(ans)