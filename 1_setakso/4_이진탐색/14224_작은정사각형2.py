from sys import stdin
I = stdin.readline

def count_pt(x, y, li, m):
    count = 0
    for i in li:
        if i[0] > x and i[0] < x + m and i[1] > y and i[1] < y + m:
            count += 1
    return count

def square(x, y, K, li):
    s = 1
    e = 10000000000
    ans = 0
    while s <= e:
        m = (s + e) // 2
        if count_pt(x, y, li, m) < K:
            s = m + 1
        else:
            ans = m
            e = m - 1
    
    if s > 10000000000:
        return 20000000000
    else:
        return ans

N, K = map(int, I().split())
X = []
Y = []
li = []
for i in range(N):
    x, y = map(int, I().split())
    X.append(x)
    Y.append(y)
    li.append([x, y])

area_list = []
for i in X:
    for j in Y:
        x_val = i - 1
        y_val = j - 1
        area_list.append(square(x_val, y_val, K, li))

print(min(area_list)**2)
