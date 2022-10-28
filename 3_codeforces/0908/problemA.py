from sys import stdin
input = stdin.readline

for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    N = max(arr)
    for i in range(n):
        if arr[i] == N:
            print(i + 1)
            break