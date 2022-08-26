def fly(D, A, B, F):
    ans = 0
    s = 0
    t = [A, B]
    while True:
        s += 1
        t = D / (t[s % 2] + F)
        ans += F * t
        m = (A + B) * t
        D -= m
        if m < 10**(-20):
            break
    return round(ans, 7)

T = int(input())
for t in range(1, T+1):
    D, A, B, F = map(int, input().split())

    print(f'#{t}', fly(D, A, B, F))