from sys import stdin, stdout
I = stdin.readline
P = stdout.write

G = int(I())

if (G % 2 == 0 and G % 4 != 0) or G == 1:
    print(-1)
    quit()

li = []
i = 1
while i * i < G:
    if G % i == 0 and (i + G // i) % 2 == 0:
       li.append((i + G // i)//2)
    i += 1

for i in li[::-1]:
    print(i)