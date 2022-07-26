from sys import stdin, stdout
I = stdin.readline
P = stdout.write

li = []
for i in range(9):
    li.append(int(I()))
li.sort()

S = sum(li) - 100

s = 0
e = len(li) - 1

while True:
    if li[s] + li[e] < S:
        s += 1
    elif li[s] + li[e] > S:
        e -= 1
    else:
        break

for i in range(9):
    if i == s or i == e:
        continue
    else:
        P(f'{li[i]}\n')