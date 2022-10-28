from sys import stdin
input = stdin.readline

for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    num = 0
    for i in range(n - 1):
        num = max(num, arr[i] - arr[i+1])
    print(max(max(arr) - arr[0], arr[n-1] - min(arr), num))