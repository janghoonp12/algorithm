from sys import stdin
I = stdin.readline

def count(N, m):
    if m == 1:
        return 1
    else:
        c = 0
        for i in range(1, N + 1):
            if m // i > N:
                c += N
            else:
                c += m // i
        return c

N = int(I())
k = int(I())

s = 1
e = 10000000000

while s <= e:
    m = (s + e) // 2
    
    if count(N, m) < k:
        s = m + 1
        
    elif count(N, m - 1) >= k:
        e = m - 1
    
    else:
        print(m)
        quit()