import math

n = int(input())
ans = 0
for i in range(1, n-1):
    for j in range(1, n - i):
        ans += math.lcm(n - (i + j), math.gcd(i, j))
        
print(ans)