# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [['1']*(N+2)] + [['1'] + list(input()) + ['1'] for _ in range(N)] + [['1']*(N+2)]

    s = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == '2':
                s = (i, j)
                break
        if s:
            break

    ans = 0
    D = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    stack = [s]
    (i, j) = s
    while True:
        for di, dj in D:
            if arr[i+di][j+dj] == '3':
                ans = 1
                break
            elif arr[i+di][j+dj] == '0':
                if arr[i][j] == '1':
                    stack.append((i, j))
                arr[i][j] = '1'
                i += di
                j += dj
                stack.append((i, j))
                break
        else:
            arr[i][j]= '1'
            try:
                (i, j) = stack.pop()
            except:
                break

        if ans == 1:
            break

    print(f'#{t} {ans}')