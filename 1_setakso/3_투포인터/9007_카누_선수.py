from sys import stdin
I = stdin.readline

T = int(I())
for i in range(T):
    k, n = map(int, I().split())
    C1 = list(map(int, I().split()))
    C2 = list(map(int, I().split()))
    C3 = list(map(int, I().split()))
    C4 = list(map(int, I().split()))

    C12 = []
    C34 = []

    for i in C1:
        for j in C2:
            C12.append(i + j)

    for i in C3:
        for j in C4:
            C34.append(i + j)

    C12.sort()
    C34.sort()

    s = 0
    e = len(C34) - 1
    D = 40000000
    q = 0

    while s < len(C12) and e > -1:
        W = C12[s] + C34[e]
        d = W - k
        
        if d > 0:
            e -= 1
        elif d < 0:
            s += 1
        else:
            ans = W
            break
        
        if abs(d) < D:
            D = abs(d)
            ans = W
        elif -d == D:
            ans = W
    print(ans)
