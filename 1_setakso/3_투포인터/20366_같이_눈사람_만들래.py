from sys import stdin
I = stdin.readline

N = int(I())
li = list(map(int, I().split()))
li.sort()
D = 2000000000

for i in range(N - 1):
    for j in range(i + 1, N):
        s = 0
        e = N - 1
        while s < e:
            if s == i or s == j:
                s += 1
                continue
            if e == i or e == j:
                e -= 1
                continue
            
            d = li[j] + li[i] - li[s] - li[e]
            if abs(d) < D:
                D = abs(d)
            if d > 0:
                s += 1
            elif d < 0:
                e -= 1
            else:
                print(0)
                quit()
                
print(D)
