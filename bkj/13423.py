from sys import stdin
I = stdin.readline

T = int(I())

for i in range(T):
    N = int(I())
    count = 0
    li = sorted(list(map(int, I().split())))
    for j in range(N-1):
        for k in range(j+1, N):
            s = 0
            e = N - 1
            if s == j or s == k:
                s += 1
            if e == j or e == k:
                e -= 1
            
            a = 2 * li[j] - li[k]
            
            while True:
                if s > e:
                    break
                
                m = (s + e) // 2
                if li[m] == a:
                    count += 1
                    break
                elif li[m] < a:
                    s = m + 1
                else:
                    e = m - 1
                    
    print(count)
