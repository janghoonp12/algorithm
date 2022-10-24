t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = min(arr)
    s = 0
    for i in arr:
        s += i - m
    print(s)
