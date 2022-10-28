from sys import stdin
I = stdin.readline

def wifi(C, li, m):
    count_f = 1
    count_b = 1
    s = 0
    e = 1
    while e < len(li):
        if li[e] - li[s] >= m:
            count_f += 1
            s = e
        e += 1
        
    s = len(li) - 1
    e = s - 1
    while e >= 0:
        if li[s] - li[e] >= m:
            count_b += 1
            s = e
        e -= 1
        
    if max(count_f, count_b) < C:
        return False
    else:
        return True

N, C = map(int, I().split())
li = []
for _ in range(N):
    li.append(int(I()))
li.sort()

s = 0
e = 1000000000
ans = 0
while s <= e:
    m = (s + e) // 2
    
    if wifi(C, li, m):
        s = m + 1
        ans = m        
    else:
        e = m - 1
        
print(ans)