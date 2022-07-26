from sys import stdin, stdout
I = stdin.readline
P = stdout.write

N, M = map(int, I().split())
li = list(map(int, I().split()))
S = 0
m = 0
count = 0

for i in li:
    S += i
    while S > M:
        S -= li[m]
        m += 1
    if S == M:
        count +=1
        S -= li[m]
        m += 1

P(f'{count}\n')