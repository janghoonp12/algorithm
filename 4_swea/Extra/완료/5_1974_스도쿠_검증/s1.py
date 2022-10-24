T = int(input())
for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    ans = 1
    for i in range(9):
        check_1 = [0]*10
        check_2 = [0]*10
        check_3 = [0]*10
        for j in range(9):
            if check_1[arr[i][j]] or check_2[arr[j][i]] or check_3[arr[i//3*3 + j//3][i%3*3 + j%3]]:
                ans = 0
                break
            else:
                check_1[arr[i][j]] += 1
                check_2[arr[j][i]] += 1
                check_3[arr[i//3*3 + j//3][i%3*3 + j%3]] += 1

        if ans == 0:
            break

    print(f'#{t}', ans)