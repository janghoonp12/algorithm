from sys import stdin
I = stdin.readline

def cut(N, li, m):
    count = 0
    for i in li:
        count += i // m
    if count < N:
        return False
    else:
        return True

K, N = map(int, I().split())
li = []
for _ in range(K):
    li.append(int(I()))

s = 1
e = 10000000000
ans = 0
while s <= e:
    m = (s + e) // 2
    
    if cut(N, li, m):
        s = m + 1
        ans = m
    else:
        e = m - 1
        
print(ans)