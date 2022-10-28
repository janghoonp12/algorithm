from sys import stdin
I = stdin.readline

c = int(I())
for _ in range(c):
    d, n = map(int, I().split())
    arr = [0] + list(map(int, I().split()))
    
    prefix = [0]*(n+1)
    for i in range(1, n+1):
        prefix[i] = arr[i] + prefix[i-1]
    
    count = [0]*d
    for i in prefix:
        count[i%d] += 1
    ans = 0
    for i in count:
        ans += i*(i-1)//2
    print(ans)