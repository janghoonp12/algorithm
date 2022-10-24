from math import gcd
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    
    n_idx = [0 for i in range(1001)]
    for i in range(1, n + 1):
        n_idx[arr[i]] = i
    
    ans = -1
    for i in range(1, 1000):
        if not n_idx[i]:
            continue
        for j in range(i, 1001):
            if not n_idx[j]:
                continue
            if gcd(i, j) == 1:
                ans = max(n_idx[i] + n_idx[j], ans)
    print(ans)