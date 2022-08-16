# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    ans = 1
    for i in range(9):
        S_h = 0
        S_v = 0
        S_s = 0
        for j in range(9):
            S_h += arr[i][j]
            S_v += arr[j][i]
            S_s += arr[i//3*3 + j//3][i%3*3 + j%3]

        if S_h != 45 or S_v != 45 or S_s != 45:
            ans = 0
            break
        
    print(f'#{t} {ans}')