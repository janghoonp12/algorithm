from sys import stdin
I = stdin.readline

T = int(I())
n = int(I())
A = [0] + list(map(int, I().split()))
m = int(I())
B = [0] + list(map(int, I().split()))

prefix_A = [0 for _ in range(n+1)]
for i in range(1, n+1):
    prefix_A[i] = A[i] + prefix_A[i-1]

prefix_B = [0 for _ in range(m+1)]
for i in range(1, m+1):
    prefix_B[i] = B[i] + prefix_B[i-1]

sub_A = {}
for i in range(n):
    for j in range(i+1, n+1):
        s = prefix_A[j] - prefix_A[i]
        sub_A[s] = sub_A.get(s, 0) + 1

ans = 0
for i in range(m):
    for j in range(i+1, m+1):
        D = T - (prefix_B[j] - prefix_B[i])
        ans += sub_A.get(D, 0)
print(ans)
        
# count_B = {}
# for i in prefix_B:
#     count_B[i] = count_B.get(i, 0) + 1