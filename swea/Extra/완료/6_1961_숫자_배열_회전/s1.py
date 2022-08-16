# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    
    print(f'#{t}')
    for i in range(N):
        for j in range(3):
            for k in range(N):
                if j == 0:
                    print(arr[N-1-k][i], end='')
                elif j == 1:
                    print(arr[N-1-i][N-1-k], end='')
                else:
                    print(arr[k][N-1-i], end='')
            print(' ', end='')
        print()
