from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 3:
        print(-1)
        continue
    elif n == 5:
        print('5 4 1 2 3')
        continue
    
    arr = [n - i for i in range(n)]
    if n % 2 == 0:
        print(*arr)
    else:
        arr[n // 2], arr[n // 2 + 1] = arr[n // 2 + 1], arr[n // 2]
        print(*arr)