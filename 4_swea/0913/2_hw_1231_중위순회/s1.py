def readtree(n):
    global ans
    
    if tree_node[n]:
        readtree(2 * n)
        ans += tree_node[n]
        readtree(2 * n + 1)


for t in range(1, 11):
    N = int(input())
    tree_node = [0] * (1<<8)
    for i in range(N):
        inp = tuple(input().split())
        tree_node[int(inp[0])] = inp[1]
    ans = ''
    readtree(1)
    
    print(f'#{t}', ans)