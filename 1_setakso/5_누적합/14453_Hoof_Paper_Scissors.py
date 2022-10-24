from sys import stdin
I = stdin.readline

N = int(I())
prefix = []
h = p = s = 0
m = 0
for _ in range(N):
    g = input()
    if g == 'H':
        h += 1
    elif g =='P':
        p += 1
    else:
        s += 1
    prefix.append([h, p, s])
for i in prefix:
    w = max(i) + max(prefix[N-1][0] - i[0], prefix[N-1][1] - i[1], prefix[N-1][2] - i[2])
    if w > m:
        m = w
print(m)