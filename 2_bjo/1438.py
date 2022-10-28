from sys import stdin
I = stdin.readline

N = int(I())
li = []
Y = []
for i in range(N):
    x, y = map(int, I().split())
    li.append([x, y])
    if y not in Y:
        Y.append(y)

li.sort()
Y.sort()
m = 200000000

for i in range(len(Y)):
    for j in range(i, len(Y)):
        X = []
        lis = []
        for k in li:
            if k[1] >= Y[i] and k[1] <= Y[j]:
                X.append(k[0])

        X.append(0)
        s = 0
        e = 0
        count = 1
        while e < len(X) - 1:
            count = e - s + 1
            if count < N//2:
                e += 1
                continue
            
            A = (Y[j] - Y[i] + 2) * (X[e] - X[s] + 2)
            if A < m:
                m = A
            s += 1
            e += 1

print(m)