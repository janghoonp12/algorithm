import sys
sys.setrecursionlimit(100010)

def dfs(cur, x):
    global possible, cnt
    
    if possible:
        return
        
    visited[x][cur] = True
    
    if cur == C - 1:
        possible = True
        cnt += 1
        return
    
    
    for i in range(3):
        nx = x + dx[i]
        
        if not 0 <= nx < R or arr[nx][cur + 1] == 'x' or visited[nx][cur + 1]:
            continue
        
        dfs(cur + 1, nx)


R, C = map(int, input().split())
arr = [input() for i in range(R)]

dx = [-1, 0, 1]
visited = [[False for i in range(C)] for j in range(R)]
temp = [0] * C
cnt = 0

for i in range(R):
    possible = False
    dfs(0, i)

print(cnt)