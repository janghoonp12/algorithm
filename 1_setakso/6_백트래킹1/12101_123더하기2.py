def recur(cur):
    S = sum(arr[:cur])

    if S >= n:
        if S == n:
            ans.append(arr[:cur])
        return
    
    for i in range(1, 4):
        arr[cur] = i
        recur(cur + 1)

n, k = map(int, input().split())
arr = [0 for i in range(n)]
ans = []

recur(0)

try:
    P = ans[k - 1]
    for i in range(len(P) - 1):
        print(P[i], end = '+')
    print(P[-1])
    
except:
    print(-1)