from sys import stdin
I = stdin.readline

def pour(K, li, m):
    g = 0
    for i in li:
        g += i // m
    if g < K:
        return False
    else:
        return True

N, K = map(int, I().split())
li = []
for _ in range(N):
    li.append(int(I()))

s = 0
e = 10000000000
ans = 0
while s <= e:
    m = (s + e) // 2
    
    if pour(K, li, m):
        s = m + 1
        ans = m
    else:
        e = m - 1
        
print(ans)