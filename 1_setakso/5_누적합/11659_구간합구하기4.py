from sys import stdin
I = stdin.readline

N, M = map(int, I().split())
arr = [0] + list(map(int, I().split()))
prefix = [0]*(N+1)

for i in range(1, N+1):
    prefix[i] = arr[i] + prefix[i-1]

for _ in range(M):
    i, j = map(int, I().split())
    print(prefix[j]-prefix[i-1])