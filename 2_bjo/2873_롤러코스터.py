import sys
input = sys.stdin.readline


R, C = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(R)]
ans = ''

if R % 2:
    ans = ('R' * (C - 1) + 'D' + 'L' * (C - 1) + 'D') * (R // 2) + 'R' * (C - 1)
elif C % 2:
    ans = ('D' * (R - 1) + 'R' + 'U' * (R - 1) + 'R') * (C // 2) + 'D' * (R - 1)
else:
    m = arr[0][1]
    x = 0
    y = 1
    for i in range(R):
        for j in range(C):
            if (i + j) % 2 == 0:
                continue
            if arr[i][j] < m:
                m = arr[i][j]
                x = i
                y = j
    if x % 2:
        ans = 'RD'
    else:
        ans = 'DR'
    ans = ('R' * (C - 1) + 'D' + 'L' * (C - 1) + 'D') * (x // 2) + ('DRUR' * (y // 2)) + ans + ('RURD' * (C // 2 - 1 - y // 2)) + ('D' + 'L' * (C - 1) + 'D' + 'R' * (C - 1)) * (R // 2 - 1 - x // 2)
print(ans)