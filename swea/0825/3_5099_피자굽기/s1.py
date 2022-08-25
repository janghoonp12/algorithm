# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))

    queue = []
    for i in range(N):
        queue.append([C[i], i + 1])
    
    k = N
    while queue:
        p = queue.pop(0)
        p[0] //= 2
        if p[0]:
            queue.append(p)
        else:
            if k == M:
                continue
            else:
                queue.append([C[k], k + 1])
                k += 1
    ans = p[1]

    print(f'#{t} {ans}')
