t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    arr = [0] + sorted(list(map(int, input().split())), reverse=True)
    
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = arr[i] + prefix[i - 1]
    
    for i in range(q):
        k = int(input())
        if k > prefix[-1]:
            print(-1)
            continue
        
        s = 0
        e = n
        while s <= e:
            m = (s + e) // 2
            if prefix[m] < k:
                s = m + 1
            else:
                e = m - 1
                ans = m
        print(ans)
