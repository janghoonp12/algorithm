from sys import stdin, stdout
I = stdin.readline
P = stdout.write

N, M = map(int, I().split())
li1 = list(map(int, I().split()))
li2 = list(map(int, I().split()))

li1.append(10**9+1)
li2.append(10**9+1)
s1 = 0
s2 = 0
li = []

while s1 != N or s2 != M:
    if li1[s1] <= li2[s2]:
        li.append(li1[s1])
        s1 += 1         
    else:
        li.append(li2[s2])
        s2 += 1
        
print(*li)