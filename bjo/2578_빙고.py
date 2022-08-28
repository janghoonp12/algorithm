from sys import stdin
I = stdin.readline

bingo = []
for _ in range(5):
    bingo.append(list(map(int, I().split())))
call = []
for _ in range(5):
    call += list(map(int, I().split()))

li = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]

for i in range(25):
    for j in range(5):
        for k in range(5):
            if call[i] == bingo[j][k]:
                li[j][k] = 1

    B = 0
    for j in range(5):
        if sum(li[j]) == 5:
            B += 1
            
    for j in range(5):
        s = 0
        for k in range(5):
            s += li[k][j]
        if s == 5:
            B += 1
    s = 0    
    for j in range(5):
         s += li[j][j]
    if s == 5:
        B += 1
    s = 0    
    for j in range(5):
         s += li[4-j][j]
    if s == 5:
        B += 1
    if B >= 3:
        print(i+1)
        quit()
        
'''
list(map(list, zip(*bingopan)))
행렬 변경

'''