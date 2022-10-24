from sys import stdin
I = stdin.readline

def give(N, lis, j):
    count = 0
    for i in lis:
        if i % j:
            count += i // j + 1
        else:
            count += i // j
    if count > N:
        return False
    else:
        return True    

N, M = map(int, I().split())
li = []
for _ in range(M):
    li.append(int(I()))
li.sort

s = 1
e = 1000000000
ans = 0
while s <= e:
    m = (s + e) // 2
    
    if give(N, li, m):
        e = m - 1
        ans = m
    else:
        s = m + 1
        
print(ans)