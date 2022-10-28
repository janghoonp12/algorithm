a, b = map(int, input().split())
'''
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
1 2 1 4 1 2 1 8 1  2  1  4  1  2  1 16  1
F(A)=f(1)+...+f(A)
what we want is F(b)-F(a-1)
F(n)= n*1(1-0) + n//2*(2-1) + n//4*(4-2)
'''

def F(n):
    i = 1
    s = n
    while 2**i <= n:
        s += (n//(2**i))*(2**i - 2**(i-1))
        i += 1
    return s

print(F(b)-F(a-1))
