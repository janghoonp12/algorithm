# import sys
# sys.stdin = open('input.txt', 'r')
def recur(cur, i, j, d):
    global fly
    y = i + d[0]
    x = j + d[1]
    
    if cur == M-1 or not 0 <= x < N or not 0 <= y < N:
        return
    
    fly += arr[y][x]
    recur(cur + 1, y, x, d)

    
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    
    D =  [[(0, 1), (1, 0), (0, -1), (-1, 0)], [(1, 1), (1, -1), (-1, -1), (-1, 1)]]
    ans = 0
    for i in range(N):
        for j in range(N):
            for delta in D:
                fly = arr[i][j]
                for d in delta:
                    recur(0, i, j, d)
                ans = max(ans, fly)
    
    print(f'#{t}', ans)