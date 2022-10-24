from sys import stdin
I = stdin.readline

n = int(I())
X, Y = [], []
for _ in range(n):
    x, y = map(int, I().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()
ans = 0
for i in range(n):
    ans += abs(X[i] - X[n//2]) + abs(Y[i] - Y[n//2])

print(ans)