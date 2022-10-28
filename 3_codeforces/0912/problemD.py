from sys import stdin
input = stdin.readline

for t in range(int(input())):
    n = int(input())
    x_arr = tuple(map(int, input().split()))
    y_arr = tuple(map(int, input().split()))
    arr = [0] * n
    for i in range(n):
        arr[i] = y_arr[i] - x_arr[i]
    arr.sort()
    s = 0
    e = n - 1
    ans = 0
    while s < e:
        if arr[s] + arr[e] < 0:
            s += 1
        else:
            ans += 1
            s += 1
            e -= 1
    print(ans)