from sys import stdin
input = stdin.readline

n = int(input())
H = list(map(int, input().split()))
A = sorted(list(map(int, input().split())))
ans = sum(H)
for i in range(n):
    ans += A[i] * i
print(ans)