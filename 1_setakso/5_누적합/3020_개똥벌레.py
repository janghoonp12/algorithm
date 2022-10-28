from sys import stdin
I = stdin.readline

N, H = map(int, I().split())

arr = [0]*(H+1)
for i in range(N):
    if i%2:
        arr[H] -= 1
        arr[H-int(I())] += 1
    else:
        arr[0] += 1
        arr[int(I())] -= 1

prefix = [0]*(H)
for i in range(H):
    prefix[i] = arr[i] + prefix[i-1]

count = 0
m = prefix[0]

for i in prefix:
    if i == m:
        count += 1
    if i < m:
        m = i
        count = 1

print(m, count)