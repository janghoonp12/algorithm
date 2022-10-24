N = int(input())
arr = [0] + sorted(list(map(int, input().split())))
prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = arr[i] + prefix[i - 1]
for i in range(1, N + 1):
    if arr[i] > prefix[i - 1] + 1:
        ans = prefix[i - 1] + 1
        break
else:
    ans = prefix[N] + 1
print(ans)