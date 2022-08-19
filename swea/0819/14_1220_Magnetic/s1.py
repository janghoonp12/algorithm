for t in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    ans = 0
    for j in range(100):
        save = 0
        for i in range(100):
            x = arr[i][j]
            if x == 1:
                save = 1
            elif x == 2 and save:
                ans += 1
                save = 0
    
    print(f'#{t}', ans)