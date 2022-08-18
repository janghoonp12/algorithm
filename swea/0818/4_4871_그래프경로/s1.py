# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    path = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        path[s].append(e)
    S, G = map(int, input().split())

    stack = [0]*(V)
    top = -1
    visited = [False]*(V+1)
    visited[S] = True
    top += 1
    stack[top] = S
    ans = 0

    while ans == 0 and top > -1:
        for i in path[stack[top]]:
            if i == G:
                ans = 1
                break
            elif visited[i] == False:
                top += 1
                stack[top] = i
                visited[i] = True
                break
        else:
            top -= 1

    print(f'#{t} {ans}')