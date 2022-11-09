N = int(input())
ans = 'YES'
if N == 0:
    ans = 'NO'
while N:
    if N % 3 == 2:
        ans = 'NO'
        break
    N //= 3
print(ans)