T = int(input())
for t in range(1, T+1):
    S = float(input())
    
    ans = ''
    for i in range(1, 13):
        if S == 0:
            break
        if S >= 1 / (1<<i):
            ans += '1'
            S -= 1 / (1<<i)
        else:
            ans += '0'
    if S:
        ans = 'overflow'
    
    print(f'#{t}', ans)