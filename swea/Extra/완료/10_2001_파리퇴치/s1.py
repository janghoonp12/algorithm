# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_F = 0
    for i in range(M-1, N):
        for j in range(M-1, N):
            S = 0
            for k in range(M):
                for l in range(M):
                    S += arr[i-k][j-l]
            if S > max_F:
                max_F = S
    print(f'#{t} {max_F}')