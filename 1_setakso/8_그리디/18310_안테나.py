from sys import stdin
input = stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))
print(arr[(N - 1) // 2])