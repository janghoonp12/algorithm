from sys import stdin
input = stdin.readline


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    v = [[] for i in range(n + 1)]
    for i in range(m):
        a, b = map(int, input().split())
        
        v[a].append(b)
    
    f = int(input())
    cost = list(map(int, input().split()))
    