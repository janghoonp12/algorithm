'''
0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15
0   1   4   9   16  25  36  49  64  81  100 121 144 169 196 225
  1   3   5   7   9   11  13  15  17  19  21  23  25  27  29  

G가 15인 경우
1. 제곱 값들 리스트 저장하고 차이 계산
    완전탐색으로는 시간초과 -> 투포인터 적용
2. 3 5 7 9 ... 홀수 리스트에서 누적합 계산
3. g = w^2 - v^2 즉 g = (w-v)(w+v) (w>v)
    w - v = a, w + v = b 면 w = (a+b)/2 v = (a-b)/2
    15 = 1*15, 3*5 => w = 16/2, 8/2
'''

from sys import stdin, stdout
I = stdin.readline
P = stdout.write

G = int(I())

square = []
for i in range(1, G // 2 + 2):
    square.append(i*i)

li = []
s = 0
e = 0
10
while e < len(square):
    if square[e] - square[s] < G:
        e += 1
    elif square[e] - square[s] > G:
        s += 1
    else:
        li.append(e+1)
        e += 1
        s += 1

if not li:
    P(f'{-1}\n')
else:
    for i in li:
        P(f'{i}\n')