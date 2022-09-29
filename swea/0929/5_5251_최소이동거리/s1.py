T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    v = [[] for i in range(N + 1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        v[s].append((e, w))
    least = [float('inf') for i in range(N + 1)]
    least[0] = 0
    
    for i in range(N + 1):
        for j in v[i]:
            least[j[0]] = min(least[j[0]], least[i] + j[1])

    ans = least[N]
    
    print(f'#{t}', ans)