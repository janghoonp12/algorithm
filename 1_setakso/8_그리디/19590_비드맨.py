from sys import stdin
input = stdin.readline

N = int(input())
arr = sorted([int(input()) for i in range(N)])
M = arr[-1]
S = sum(arr) - M
if M >= S:
    ans = M - S
else:
    ans = (S - M) % 2
print(ans)
