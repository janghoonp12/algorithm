T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]
    find = [0] + [1]*K +[0]

    ans = 0
    for i in range(1, N+1):
        for j in range(N-K+1):
            for k in range(K+2):
                if arr[i][j+k] != find[k]:
                    break
            else:
                ans += 1

            for k in range(K+2):
                if arr[j+k][i] != find[k]:
                    break
            else:
                ans += 1
    
    print(f'#{t}', ans)