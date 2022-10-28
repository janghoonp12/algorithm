def recur(cur, damage, hp, point, last_ppl):
    global ans
    
    if hp < 0:
        ans = max(ans, point - last_ppl)
        return
    elif cur == N:
        ans = max(ans, point)
        return

    
    recur(cur + 1, damage + Atk[cur], hp - damage - Atk[cur], point + Ppl[cur], Ppl[cur])
    recur(cur + 1, damage, hp, point, last_ppl)

N, K = map(int, input().split())
Atk = tuple(map(int, input().split()))
Ppl = tuple(map(int, input().split()))

ans = 0

recur(0, 0, K, 0, 0)

print(ans)