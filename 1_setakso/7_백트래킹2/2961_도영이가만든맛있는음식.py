def recur(cur, sour, bitter):
    global ans
    
    if cur == N:
        if bitter == 0:
            return
        else:
            ans = min(ans, abs(bitter - sour))
            return
            
    recur(cur + 1, sour * arr[cur][0], bitter + arr[cur][1])
    recur(cur + 1, sour, bitter)

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
ans = 1000000000
recur(0, 1, 0)

print(ans)