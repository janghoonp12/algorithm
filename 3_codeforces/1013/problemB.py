from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    ans = 'YES'
    for i in range(n - 1):
        if arr[i + 1] <= arr[i]:
            ans = 'NO'
            break
    print(ans)