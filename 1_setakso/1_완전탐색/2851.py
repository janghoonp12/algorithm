mush = []
point = 0
p = 0
for i in range(10):
    mush.append(int(input()))
for j in range(10):
    if abs(point-100)>=abs(point+mush[j]-100):
        p = point+mush[j]
    point = point+mush[j]
print(p)
