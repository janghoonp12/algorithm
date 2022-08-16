# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    ans = ''
    for i in range(N):
        if ans:
            break
        for j in range(N-M+1):
            count_h = count_v = 0

            for k in range(M//2):
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    break
                else:
                    count_h += 1

            for k in range(M//2):
                if arr[j+k][i] != arr[j+M-1-k][i]:
                    break
                else:
                    count_v += 1

            if count_h == M//2:
                for k in range(M):
                    ans += arr[i][j+k]
                break

            if count_v == M//2:
                for k in range(M):
                    ans += arr[j+k][i]
                break
    
    print(f'#{t} {ans}')