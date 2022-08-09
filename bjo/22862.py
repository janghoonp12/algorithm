from sys import stdin
I = stdin.readline

N, K = map(int, I().split())
li = list(map(int, I().split()))

s = 0
e = 0
if li[0] % 2:
    ec = 0
    oc = 1
else:
    ec = 1
    oc = 0
L = ec

while e < N - 1:

    if oc <= K:
        e += 1
        if li[e] % 2:
            oc += 1
    else:
        if li[s] % 2:
            oc -= 1
        s += 1
    
    ec = e - s + 1 - oc
    if ec > L:
        L = ec

print(L)
