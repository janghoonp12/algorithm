N = int(input())

m = 0
for i in range(N + 1):
    li = [N, i]
    d = 0
    i = 1
    while True:
        d = li[i-1] - li[i]
        if d < 0:
            break
        li.append(d)
        i += 1
    if len(li) > m:
        m = len(li)
        m_li = li[:]
print(m)
print(*m_li)