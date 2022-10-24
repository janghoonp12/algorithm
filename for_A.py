T = int(input())
for t in range(1, T + 1):
    Ms, Ma = map(int, input().split())
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    ms = Ms
    for i in range(L):
        profit = [0 for i in range(N)]
        for j in range(N):
            profit[j] = arr[j][i + 1] - arr[j][i]
        
        dp = [0 for i in range(Ms + 1)]
        for j in range(Ms + 1):
            m = 0
            for k in range(N):
                if j - arr[k][i] < 0:
                    continue
                m = max(m, dp[j - arr[k][i]] + profit[k])
            dp[j] = m
        Ms += dp[Ms] + Ma
    
    print(f'#{t}', Ms - ms - L * Ma)