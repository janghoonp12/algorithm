T = int(input())
for _ in range(T):
    n, k, b, s = map(int, input().split())
    if s < k*b or s > b*(2*k-1) + (n-b)*(k-1):
        print(-1)
        continue
    else:
        arr = []
        if s >= k*(b+1):
            arr.append(k*(b+1)-1)
            s -= k*(b+1)-1
        else:
            arr.append(s)
            s = 0
        for i in range(n-1):
            if s > k-1:
                arr.append(k-1)
                s -= k-1
            else:
                arr.append(s)
                s =0
    print(*arr)
