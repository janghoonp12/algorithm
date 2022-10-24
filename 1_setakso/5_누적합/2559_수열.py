from sys import stdin
I = stdin.readline

N, K = map(int, I().split())
arr = [0] + list(map(int, I().split()))
prefix = [0]*(N+1)

for i in range(1, N+1):
    prefix[i] = arr[i] + prefix[i-1]

ans = prefix[K]
for i in range(K, N+1):
    ans = max(ans, prefix[i] - prefix[i-K])

print(ans)