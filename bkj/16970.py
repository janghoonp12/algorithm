from sys import stdin, stdout
from math import gcd

I = stdin.readline
P = stdout.write

N, M, K = map(int, I().split())

if K > N + 1 and K > M + 1:
    P('0\n')
    quit()

count = 0
for i in range(N + 1):
    for j in range(M + 1):
        for k in range(N + 1):
            for l in range(M + 1):
                if gcd(k - i, l - j) == K-1:
                    count += 1
P(f'{count//2}\n')


'''
10  3 3 3 3 3 1 3 3 3 3 3
9   3 3 3 3 3 1 3 3 3 3 3
8   3 3 3 3 3 1 3 3 3 3 3
7   3 3 3 3 3 1 3 3 3 3 3
6   3 3 3 3 3 1 3 3 3 3 3
5   1 1 1 1 1 0 1 1 1 1 1
4   3 3 3 3 3 1 3 3 3 3 3
3   3 3 3 3 3 1 3 3 3 3 3
2   3 3 3 3 3 1 3 3 3 3 3
1   3 3 3 3 3 1 3 3 3 3 3
0   3 3 3 3 3 1 3 3 3 3 3

x   0 1 2 3 4 5 6 7 8 9 10

ex) 9 9 4(중간에 점 2개)
0,0 1,0 2,0 3,0         
0,0 2,1 4,2 6,3 gcd()=3         
0,0 3,1 6,2 9,3
0,0 3,2 6,4 9,6
K-1의 배수랑 관련 있음

안되는거 0,0 2,0 4,0 6,0 왜? 2,3 둘다 겹쳐서 안됨

'''