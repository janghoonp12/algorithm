from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
arr = [[] for i in range(11)]
for i in range(N):
    C, G = map(int, input().split())
    arr[G].append(C)

for i in range(11):
    arr[i].sort(reverse=True)
    
suffix = [[0 for i in range(N + 1)] for j in range(11)]
for i in range(1, 11):
    for j in range(1, N + 1):
        if j > len(arr[i]):
            break
        suffix[i][j] = arr[i][j - 1] + suffix[i][j - 1] + 2 * (j - 1)

dp = [0 for i in range(K + 1)]
idx = [[0 for i in range(11)] for j in range(K + 1)]

for i in range(1, K + 1):
    for j in range(1, i + 1):
        for k in range(1, 11):
            if suffix[k][idx[i - j][k] + j] == 0:
                continue
            temp = dp[i - j] + suffix[k][idx[i - j][k] + j] - suffix[k][idx[i - j][k]]
            if temp > dp[i]:
                dp[i] = temp
                for l in range(1, 11):
                    idx[i][l] = idx[i - j][l]
                idx[i][k] += j

print(dp[K])