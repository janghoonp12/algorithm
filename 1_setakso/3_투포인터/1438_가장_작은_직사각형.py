from sys import stdin
I = stdin.readline

N = int(I())
X = []
Y = []
for i in range(N):
    x, y = map(int, I().split())
    X.append(x)
    Y.append(y)

if N == 2:
    print(4)
    quit()

A = 10002*10002
for i in range(N-1):
    x1 = X[i]
    for j in range(i+1,N):
        x2 = X[j]
        for k in range(N-1):
            y1 = Y[k]
            for l in range(k+1,N):
                y2 = Y[l]
                count = 0
                for i in range(N):
                    if X[i] > min(x1, x2)-1 and X[i] < max(x1, x2)+1 and Y[i] > min(y1, y2)-1 and Y[i] < max(y1, y2)+1:
                        count += 1
                a = (abs(x2 - x1)+2) * (abs(y2 - y1)+2)        
                if count >= N//2 and a < A:
                    A = a

print(A)