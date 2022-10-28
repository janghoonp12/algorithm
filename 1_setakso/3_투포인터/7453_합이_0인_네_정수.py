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

AB = {}
for i in A:
    for j in B:
        x = i + j
        if x in AB:
            AB[x] += 1
        else:
            AB[x] = 1
            
count = 0
for i in C:
    for j in D:
        count += AB.get(-(i + j), 0)

print(count)