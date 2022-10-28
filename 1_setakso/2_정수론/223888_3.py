a, d = map(int, input().split())
q = int(input())
data = []
for k in range(q):
    data.append(list(map(int, input().split())))
t=0
for k in range(q):
    t = max(t,data[k][2])
seq = []
for i in range(t+10):
    seq.append(a+d*i)


def gcdt(b, c):
    while b%c!=0:
        g = b
        b = c
        c = g%c
    return c


def gcdlist(x):
    gc = x[0]
    for j in range(len(x)):
        gc = gcdt(gc,x[j])
    return gc


for k in range(q):
    s = data[k][0]
    l = data[k][1]
    r = data[k][2]
    se = seq[l-1:r]
    if s == 1:
        an = sum(se)
    elif s == 2:
        an = gcdlist(se)
    print(an)
