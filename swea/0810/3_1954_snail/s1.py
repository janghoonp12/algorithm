import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    a = 0
    k = 1
    i = j = 0
    while k <= N * N:
        if 0 <= i < N and 0 <= j < N and arr[i][j] == 0:
                arr[i][j] = k
                k += 1
                i += di[a % 4]
                j += dj[a % 4]
        else:
            i -= di[a % 4]
            j -= dj[a % 4]
            a += 1
            i += di[a % 4]
            j += dj[a % 4]
    print(f'#{t}')
    for i in arr:
        print(*i)