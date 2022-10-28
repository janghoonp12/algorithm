import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline
print = sys.stdout.write


def dfs(cur, prv):
    color_cnt[cur][arr[cur]] += 1               
    for nxt in v[cur]:
        if nxt == prv:
            continue
        
        parent[nxt] = cur
        dfs(nxt, cur)
        for i in range(2):
            color_cnt[cur][i] += color_cnt[nxt][i]


N = int(input())
arr = [-1] + list(map(int, input().split()))
v = [[] for i in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

color_cnt = [[0] * 2 for i in range(N + 1)]
parent = [0 for i in range(N + 1)]

dfs(1, 0)


Q = int(input())
for i in range(Q):
    q = int(input())
    ans = 0
    
    C = len(v[q])
    blue = []
    red = []
    for j in v[q]:
        if j == parent[q]:
            continue
        ans -= color_cnt[j][0] * color_cnt[j][1]
        if color_cnt[j][0]:
            blue.append(color_cnt[j][0])
        if color_cnt[j][1]:
            red.append(color_cnt[j][1])
    ans -= (color_cnt[1][0] - color_cnt[q][0]) * (color_cnt[1][1] - color_cnt[q][1])
    blue.append(color_cnt[1][0] - color_cnt[q][0])
    red.append(color_cnt[1][1] - color_cnt[q][1])
    
    for j in range(len(blue)):
        for k in range(len(red)):
            ans += blue[j] * red[k]
    print(f'{ans}\n')