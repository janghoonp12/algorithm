from collections import deque


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(M)]
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())

 


que = deque()



'''
x           y           d

x + 3dx     y + 3dy     d
x + 2dx     y + 2dy     d
x + dx      y + dy      d
x           y           d1
x           y           d2
x           y           d3

'''