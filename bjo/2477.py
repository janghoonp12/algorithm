K = int(input())
li = []

for i in range(6):
    li.append(list(map(int, input().split())))

li1 = [li[0][1], li[2][1], li[4][1]]
li2 = [li[1][1], li[3][1], li[5][1]]
a = max(li1)
b = max(li2)

for i in range(6):
    c1 = li[i][0] == 3 and li[i - 1][0] == 1
    c2 = li[i][0] == 1 and li[i - 1][0] == 4
    c3 = li[i][0] == 4 and li[i - 1][0] == 2
    c4 = li[i][0] == 2 and li[i - 1][0] == 3
    if c1 or c2 or c3 or c4:
        c = li[i][1]
        d = li[i - 1][1]
        break
A = a * b - c * d
ans = A * K
print(ans)