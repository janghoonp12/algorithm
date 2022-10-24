def recur(cur):
    if (c - cur) % 2 == 0:
        arr.append(n[:])
    
    if c == cur:
        return
    
    tk = False
    for i in range(k - 1):
        for j in range(i + 1, k):
            if n[i] < n[j]:
                tk = True
                n[i], n[j] = n[j], n[i]
                recur(cur + 1)
                n[i], n[j] = n[j], n[i]
    if not tk:
        n[-1], n[-2] = n[-2], n[-1]
        recur(cur + 1) 
        n[-1], n[-2] = n[-2], n[-1] 


T = int(input())
for t in range(1, T + 1):
    n, c = input().split()
    n = list(n)
    c = int(c)
    k = len(n)
    arr = []
    
    recur(0)
    
    print(max(arr))