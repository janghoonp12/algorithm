from sys import stdin
I = stdin.readline

W, H = map(int, I().split())
N = int(I())

li_0 = [0, W]
li_1 = [0, H]

for _ in range(N):
    n, m = map(int, I().split())
    if n == 1:
        li_0.append(m)
    else:
        li_1.append(m)
li_0.sort()
li_1.sort()

w_max = 0
for i in range(len(li_0)-1):
    d = li_0[i+1] - li_0[i]
    if d > w_max:
        w_max = d

h_max = 0
for i in range(len(li_1)-1):
    d = li_1[i+1] - li_1[i]
    if d > h_max:
        h_max = d

print(w_max * h_max)