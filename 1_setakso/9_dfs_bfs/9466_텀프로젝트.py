import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline

def dfs(k):
    global cnt
    
    if visited[k]:
        if k in arr:
            cnt += len(arr) - arr.index(k)
        return
    
    visited[k] = True
    arr.append(k)
    
    dfs(v[k])


T = int(input())
for t in range(T):
    n = int(input())
    v = [0] + list(map(int, input().split()))
    visited = [False for i in range(n + 1)]
    
    cnt = 0
    for i in range(1, n + 1):
        arr = []
        dfs(i)
    
    print(n - cnt)