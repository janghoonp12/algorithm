# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    arr = [list(map(int, input().split())) for i in range(9)]
    ans = 1
    fin = False
    for i in range(9):
        if fin:
            break
        check_b = [0 for i in range(10)]
        check_r = [0 for i in range(10)]
        check_c = [0 for i in range(10)]
        for j in range(9):
            if check_r[arr[i][j]] or check_c[arr[j][i]] or check_b[arr[(i//3)*3 + j//3][(i%3)*3 + j%3]]:
                ans = 0
                fin = True
                break
            check_r[arr[i][j]] += 1
            check_c[arr[j][i]] += 1
            check_b[arr[(i//3)*3 + j//3][(i%3)*3 + j%3]] += 1
    
    print(f'#{t} {ans}')
