from sys import stdin, stdout
I = stdin.readline
P = stdout.write

n = int(I())
li = list(map(int, I().split()))
x = int(I())

li.sort()
count = 0
s = 0
e = len(li) - 1

while s < e:
    if li[s] + li[e] > x:
        e -= 1
    elif li[s] + li[e] < x:
        s += 1
    else:
        count += 1
        s += 1
        e -+ 1

P(f'{count}\n')

'''
1245689 합쳐서 9 되는 순서쌍 수?
s     e 10
     e   9
 s  e    8
  s e   10
  se     9 



'''
