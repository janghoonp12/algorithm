n, m = map(int, input().split())

ans = 1
for i in range(min(m, n - m)):
    ans *= n - i
    ans //= i + 1

print(ans)
