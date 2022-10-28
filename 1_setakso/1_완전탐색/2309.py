h = []
esk = 0
for i in range(9):
    h.append(int(input()))
s = sum(h)
for j in range(9):
    for k in range(j+1, 9):
        if s - h[j] - h[k] == 100:
            del h[k]
            del h[j]
            esk = 1
            break
    if esk == 1:
        break
h.sort()
for l in range(7):
    print(h[l])
