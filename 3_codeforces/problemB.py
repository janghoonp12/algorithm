from sys import stdin, stdout
I = stdin.readline
P = stdout.write

t = int(I())
for _ in range(t):
    n, x = map(int, I().split())
    li = list(map(int, I().split()))

    s = 0
    e = 0
    count = 0
    
    while e < n:
        if e:
            count += 1
            s = e
        
        M = li[s]
        m = li[s]
        
        while M - m <= 2 * x:
            e += 1
            if e == n:
                break
            
            if li[e] > M:
                M = li[e]
            elif li[e] < m:
                m = li[e]
    P(f'{count}\n')