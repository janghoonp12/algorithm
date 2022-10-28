# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    
    ans = 0
    count = 0
    for i in range(N):
        for j in range(M):
            if not arr[i][j]:
                ans = max(ans, count)
                count = 0
            count += arr[i][j]
        ans = max(ans, count)
        count = 0
            
    for j in range(M):
        for i in range(N):
            if not arr[i][j]:
                ans = max(ans, count)
                count = 0
            count += arr[i][j]
        ans = max(ans, count)
        count = 0
    
    print(f'#{t}', ans)