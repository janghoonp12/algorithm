from sys import stdin, stdout
I = stdin.readline
P = stdout.write

N = int(I())
li = list(map(int, I().split()))
s = 0
e = N - 1
d = li[s] + li[e]
Ab = 1000000000
Le = li[s]
Ri = li[e]

while s < e:
    S = li[s] + li[e]
    
    if abs(S) <= Ab:
        Le = li[s]
        Ri = li[e]
        Ab = abs(S)

    if S < 0:
        s += 1
    elif S > 0:
        e -= 1
    else:
        P(f'{li[s]} {li[e]}\n')
        quit()
P(f'{Le} {Ri}\n')