N = int(input())
arr = sorted([list(map(int, input().split())) for i in range(N)])
y_idx = sorted([arr[i][1] for i in range(N)])
ans = float('INF')

for i in range(N):
    for j in range(i, N):
        x_idx = []
        for k in range(N):
            if y_idx[i] <= arr[k][1] <= y_idx[j]: 
                x_idx.append(arr[k][0])
        x_idx.sort()
        
        s = e = 0
        while e < len(x_idx):
            cnt = e - s + 1
            if cnt < N // 2:
                e += 1
            else:
                A = (y_idx[j] - y_idx[i] + 2) * (x_idx[e] - x_idx[s] + 2)
                ans = min(ans, A)
                s += 1
print(ans)