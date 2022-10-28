# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    node = [[] for i in range(V + 1)]
    for i in range(E):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    S, G = map(int, input().split())

    visited = [0 for i in range(V + 1)]
    queue = [S]
    ans = 0
    while queue:
        v = queue.pop(0)
        if v == G:
            ans = visited[v]
            break

        for i in node[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[v] + 1

    print(f'#{t} {ans}')
