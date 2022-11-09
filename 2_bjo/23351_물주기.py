N, K, A, B = map(int, input().split())
arr = [K for i in range(N)]
day = 1
w = 0
while True:
    for i in range(A):
        arr[w + i] += B
    for i in range(N):
        arr[i] -= 1
    if 0 in arr:
        break
    day += 1
    w += A
    if w >= N:
        w = 0
print(day)