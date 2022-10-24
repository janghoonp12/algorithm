from sys import stdin
input = stdin.readline

for t in range(int(input())):
    s = input()[:-1]
    n = ord(s[0])
    m = ord(s[-1])
    N = min(n, m)
    M = max(n, m)
    arr = []
    for i in range(1, len(s) - 1):
        k = ord(s[i])
        if N <= k <= M:
            arr.append((k, i + 1))
    cost = M - N
    ans_m = len(arr) + 2
    print(cost, ans_m)
    if n <= m:
        arr.sort()
    else:
        arr.sort(reverse=True)
    print(1, end=' ')
    for i in arr:
        print(i[1], end=' ')
    print(len(s))