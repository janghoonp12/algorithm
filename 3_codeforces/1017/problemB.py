from sys import stdin
input = stdin.readline

for t in range(int(input())):
    n = int(input())
    arr = [i for i in range(1, n + 1)]
    arr[1], arr[n - 1] = arr[n - 1], arr[1]
    print(*arr)