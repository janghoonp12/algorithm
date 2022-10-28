from sys import stdin
I = stdin.readline

N, d, k, c = map(int,I().split())
li = []
for i in range(N):
    li.append(int(I()))
li += li[:k-1]

ct = [0] * (d + 1)
ct[c] = 1


s = 0
e = k-1
for i in range(k):
    ct[li[i]] += 1

C = 0
for i in ct:
    if i:
        C += 1
if C == k + 1:
    print(C)
    quit()
M = C

while s < N - 2:
    ct[li[s]] -= 1
    if ct[li[s]] == 0:
        C -= 1
    s += 1
    e += 1
    if ct[li[e]] == 0:
        C += 1
    ct[li[e]] += 1

    if C == k + 1:
        print(C)
        quit()
    elif C > M:
        M = C
        
print(M)



'''
0   1   2                   N-1 N       N+d-2
7   9   7   30  2   7   9   25  7   9   7
s   
e

1   2   3   4   5   6   7   8   9   10
                        2       1
11  12  13  14  15  16  17  18  19  20

21  22  23  24  25  26  27  28  29  30
                                    2
'''