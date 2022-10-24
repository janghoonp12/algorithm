from sys import stdin, stdout
from math import gcd

I = stdin.readline
P = stdout.write

a, d = map(int, I().split())
q = int(I())
G = gcd(a, d)

for i in range(q):
    c, l, r = map(int, I().split())
    if c == 1:
        P((2*a+(l+r-2)*d)*(r-l+1)//2)
    elif l == r:
        P(a+(l-1)*d)
    else:
        P(G)
