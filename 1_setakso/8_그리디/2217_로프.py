from sys import stdin
input = stdin.readline

N = int(input())
arr = [int(input()) for i in range(N)]
arr.sort(reverse=True)
arr = [0] + arr
ans = 0
for i in range(1, N + 1):
    ans = max(ans, i * arr[i])
print(ans)