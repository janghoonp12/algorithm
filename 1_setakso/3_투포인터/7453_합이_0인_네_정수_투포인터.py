from sys import stdin
I = stdin.readline

A, B, C, D = [], [], [], []
n = int(I())
for i in range(n):
    a, b, c, d = map(int, I().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
AB = []
CD = []
for i in A:
    for j in B:
        AB.append(i+j)
for i in C:
    for j in D:
        CD.append(i+j)
AB.sort()
CD.sort()

s = 0
e = len(CD) - 1
count = 0

while s < len(AB) and e > -1:
    X = AB[s] + CD[e]
    if X > 0:
        e -= 1
    elif X < 0:
        s += 1
    else:
        u, v = s, e
        while s < len(AB) - 1 and AB[s] == AB[s + 1]:
            s += 1
        while e > 0 and CD[e] == CD[e-1]:
            e -= 1
        s += 1
        e -= 1
        count += (s - u) *(v - e)
        
print(count)