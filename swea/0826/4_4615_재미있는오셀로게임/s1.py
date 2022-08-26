# import sys
# sys.stdin = open('input.txt', 'r')


def flip(i, j, d, c):
    global check

    if not 0 <= i < N or not 0 <= j < N:
        return

    if arr[i][j] == c:
        check = True
        return

    if arr[i][j] == 3 - c:
        flip(i + d[0], j + d[1], d, c)
        if check:
            arr[i][j] = c


def play(i, j, c):
    global check

    arr[i][j] = c
    for d in D:
        check = False
        flip(i + d[0], j + d[1], d, c)


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for i in range(N)]
    arr[N // 2 - 1][N // 2] = arr[N // 2][N // 2 - 1] = 1
    arr[N // 2 - 1][N // 2 - 1] = arr[N // 2][N // 2] = 2
    D = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    check = False

    for k in range(M):
        i, j, c = map(int, input().split())
        play(i - 1, j - 1, c)

    ans = [0, 0]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                ans[0] += 1
            elif arr[i][j] == 2:
                ans[1] += 1
    
    print(f'#{t}', *ans)
