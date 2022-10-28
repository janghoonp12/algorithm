from sys import stdin
I = stdin.readline

def tree(h, lis):
    total = 0
    for i in lis:
        r = i - h
        if r > 0:
            total += r
    return total

N, M = map(int, I().split())
li = list(map(int, I().split()))
            
s = 0
e = 1000000000
ans = 0
while s <= e:
    m = (s + e) // 2
    t = tree(m, li) 
    if t < M:
        e = m - 1
    else:
        s = m + 1
        ans = m
        
print(ans)