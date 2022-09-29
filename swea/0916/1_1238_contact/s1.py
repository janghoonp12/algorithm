# import sys
# sys.stdin = open('input.txt', 'r')

def emergency():
    global ans
    
    if queue:
        a, s = queue.pop(0)
        
        if s > ans[0]:
            ans = [s, a]
        elif s == ans[0]:
            ans[1] = max(ans[1], a)

        for i in path[a]:
            if not visited[i]:
                queue.append((i, s + 1))
                visited[i] = True
        emergency()
                

for t in range(1, 11):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    path = [[] for i in range(101)]
    for i in range(N // 2):
        path[arr[2 * i]].append(arr[2 * i + 1])
    visited = [False] * 101
    visited[S] = True
    queue = [(S, 1)]
    ans = [1, S]
    
    emergency()
    
    print(f'#{t}', ans[1])