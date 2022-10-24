from sys import stdin
input = stdin.readline

N = int(input())
arr = [int(input()) for i in range(N)][::-1]
ans = 0
for i in range(1, N):
    ans += max(0, arr[i] - arr[i - 1] + 1)
    arr[i] = min(arr[i], arr[i - 1] - 1)
print(ans)