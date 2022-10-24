t = int(input())
for _ in range(t):
    n, k, r, c = map(int, input().split())
    arr = [['.']*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i + j) % k == (r + c - 2) % k:
                arr[i][j] = 'X'
    for i in arr:
        for j in i:
            print(j, end='')
        print()