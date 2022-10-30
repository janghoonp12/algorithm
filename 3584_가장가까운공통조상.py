import sys
sys.setrecursionlimit(100000000)

def dfs(cur):
    for nxt in v[cur]:
        par[nxt] = cur
        dfs(nxt)
        

T = int(input())
for t in range(T):
    N = int(input())
    v = [[] for i in range(N + 1)]
    check = [0 for i in range(N + 1)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        v[a].append(b)
        check[b] = a
    n1, n2 = map(int, input().split())
    
    s = check[1:].index(0) + 1
    par = [0 for i in range(N + 1)]

    dfs(s)
    
    A1 = []
    A2 = []
    while n1:
        A1.append(n1)
        n1 = par[n1]
    while n2:
        A2.append(n2)
        n2 = par[n2]
    A1 = A1[::-1]
    A2 = A2[::-1]
    ans = s
    for i in range(min(len(A1), len(A2))):
        if A1[i] == A2[i]:
            ans = A1[i]
        else:
            break
    print(ans)