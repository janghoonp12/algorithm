t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(2 * (max(arr) - min(arr)))