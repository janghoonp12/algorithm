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

def find(y, li):
    s = 0
    e = len(li)
    while s <= e:
        m = (s + e) // 2
        if li[m][1] < y:
            s = m + 1
        elif li[m][1] > y:
            e = m - 1
        else:
            return 1
    return 0

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
    
    li1 = li[x1_lower:x1_upper]
    li2 = li[x2_lower:x2_upper]
    li1.append([2000000000, 2000000000])
    li2.append([2000000000, 2000000000])
    
    count += find(y2, li1)
    count += find(y1, li2)
    count += find(y2, li2)
        
    if count == 3:
        real_count += 1

print(real_count)