# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    count = 0
    arr = [[0]*10 for _ in range(10)]
    for _ in range(N):
        x1, y1, x2, y2, c = map(int, input().split())
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if arr[i][j] == 0:
                    arr[i][j] += c
                elif arr[i][j] + c == 3:
                    arr[i][j] += c
                    count += 1
    print(f'#{t} {count}')
