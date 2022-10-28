from sys import stdin
I = stdin.readline

N, K = map(int, I().split())
arr = [0] + list(map(int, I().split()))
prefix = [0 for _ in range(N+1)]

for i in range(1, N+1):
    prefix[i] = prefix[i-1] + arr[i]

# 2중 for문 시간초과!
# count = 0
# for i in range(N):
#     for j in range(i + 1, N + 1):
#         if prefix[j] - prefix[i] == K:
#             count += 1
# print(count)

count = {}
ans = 0
for i in prefix:
    ans += count.get(i - K, 0)
    count[i] = count.get(i, 0) + 1

print(ans)
