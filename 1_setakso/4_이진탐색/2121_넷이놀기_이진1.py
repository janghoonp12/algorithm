from sys import stdin
I = stdin.readline

def upper(li, x, N):
    s = 0
    e = N
    x_upper = 0
    while s <= e:
        m = (s + e) // 2
        if li[m][0] <= x:
            s = m + 1
        else:
            x_upper = m
            e = m - 1
    return x_upper

def lower(li, x, N):
    s = 0
    e = N
    x_lower = 0
    while s <= e:
        m = (s + e) // 2
        if li[m][0] < x:
            s = m + 1
        else:
            x_lower = m
            e = m - 1
    return x_lower
    

N = int(I())
A, B = map(int, I().split())
li = []
for _ in range(N):
    li.append(list(map(int, I().split())))

li.sort()
li.append([2000000000, 2000000000])
real_count = 0
for i in li[:N]:
    count = 0
    x1 = i[0]
    x2 = i[0] + A
    y1 = i[1]
    y2 = i[1] + B
    
    x1_upper = upper(li, x1, N)
    x1_lower = lower(li, x1, N)
    x2_upper = upper(li, x2, N)
    x2_lower = lower(li, x2, N)        
            
    for j in li[x1_lower:x1_upper]:
        if [x1, y2] == j:
            count += 1
    for j in li[x2_lower:x2_upper]:
        if [x2, y1] == j:
            count += 1
        if [x2, y2] == j:
            count += 1
    
    if count == 3:
        real_count += 1

print(real_count)