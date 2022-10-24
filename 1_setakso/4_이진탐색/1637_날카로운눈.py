from sys import stdin
I = stdin.readline

def count_num(li, m, t):
    count = 0
    for i in li:
        if m < i[0]:
            continue
        elif m >= i[1]:
            count += (i[1] - i[0]) // i[2] + 1
        else:
            count += (m - i[0]) // i[2] + 1
    
    if t != 0:
        return count
    elif count % 2:
        return True
    else:
        return False

li = []
N = int(I())
for _ in range(N):
    li.append(list(map(int, I().split())))

s = 1
e = 2**32
ans = (0, 0)

if not count_num(li, e, 0):
    print('NOTHING')
    quit()

while s <= e:
    m = (s + e) // 2
    if count_num(li, m, 0):
        e = m - 1
        ans = m
    else:
        s = m + 1    

print(ans, count_num(li, ans, 1)-count_num(li, ans - 1, 1))
