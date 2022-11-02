def F(N):
    if N == 0:
        return 0
    
    k = 0
    while N >= 1<<k:
        k += 1
    m = 1<<(k - 1)
    
    if N + 1 == 1<<k:
        return k * (2 ** (k - 1))
    
    elif N == m:
        return F(N - 1) + 1
        
    else:
        return F(m - 1) + (N - m + 1) + F(N - m)


A, B = map(int, input().split())
print(F(B) - F(A - 1))