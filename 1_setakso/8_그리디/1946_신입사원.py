from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = sorted([list(map(int, input().split())) for i in range(N)])
    ans = 1
    check = arr[0][1]
    for i in range(1, N):
        if arr[i][1] < check:
            ans += 1
            check = arr[i][1]
    print(ans)