from sys import stdin
input = stdin.readline

for t in range(int(input())):
    n, m = map(int, input().split())
    arr = [1] * n
    
    if n == 1:
        print('Yes')
        print(m)
        continue
    
    elif m < n:
        print('No')
        continue
    
    elif n % 2:
        arr[-1] = m - n + 1
        print('Yes')
        print(*arr)
        continue
    
    elif m % 2 == 0:
        k = (m - n + 2)//2
        arr[-1] = k
        arr[-2] = k
        print('Yes')
        print(*arr)
        continue
    
    else:
        print('No')
