t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [input() for i in range(n)]
    ans = 10000000000
    for i in range(n - 1):
        for j in range(i + 1, n):
            s = 0
            for k in range(m):
                s += abs(ord(arr[i][k]) - ord(arr[j][k]))
            ans = min(ans, s)
    print(ans)
