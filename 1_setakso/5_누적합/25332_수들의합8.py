from sys import stdin
I = stdin.readline

N = int(I())
A = [0] + list(map(int, I().split()))
B = [0] + list(map(int, I().split()))

arr = [0]*(N+1)
for i in range(N+1):
    arr[i] = A[i] - B[i]

prefix = [0]*(N+1)
for i in range(1, N+1):
    prefix[i] = arr[i] + prefix[i-1]

cnt = {}
ans = 0
for i in prefix:
    ans += cnt.get(i, 0)
    cnt[i] = cnt.get(i, 0) + 1

print(ans)