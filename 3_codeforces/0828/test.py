t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    arr = [0] + sorted(list(map(int, input().split())), reverse=True)
    prefix = [0] * (n + 1)
    
    for i in range(1, n + 1):
        prefix[i] = arr[i] + prefix[i - 1]
    
    fin = False
    for i in range(q):
        m = int(input())
        for j in range(n + 1):
            if prefix[j] >= m:
                print(j)
                fin = True
                break
        else:
            print(-1)
