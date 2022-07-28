# 이진탐색 풀이

from sys import stdin
I = stdin.readline

N = int(I())
A = sorted(list(map(int, I().split())))
M = int(I())
B = list(map(int, I().split()))

for i in B:
    s = 0
    e = N - 1
    while True:
        if s > e:
            u = s
            break
        m = (s + e) // 2
        if A[m] <= i:
            s = m + 1
        else:
            e = m - 1
    
    s = 0
    e = N - 1
    while True:
        if s > e:
            l = s
            break
        m = (s + e) // 2
        if A[m] < i:
            s = m + 1
        else:
            e = m - 1
    
    print(u - l, end=' ')

'''

find 7
1. find 7 upper bound
if m == 7, s = m + 1
0   1   2   3   4   5   6   7   8   9   10  11
0   1   2   3   4   5   6   7   7   7   8   9
s                                           e
                    m   
                        s                   e
                                m
                                    s       e
                                        m
                                    se
                                    m
                                    e   s


                                    7   7
                                    s   e
                                    m
                                        se
                                        m
                                        e   s

2. find 7 lower bound
if m == 7, e = m - 1
0   1   2   3   4   5   6   7   8   9   10  11
0   1   2   3   4   5   6   7   7   7   8   9
s                                           e
                    m
                        s                   e
                                m
                        s   e
                        m
                            se
                            m
                        e   s


0   1   2   3   4   5   6   7   8   9   10  11
0   1   2   3   4   5   7   7   7   7   8   9
s                                           e
                    m
                        s                   e
                                m
                        s   e
                        m
                    e   s



1   1   2
s   m   e
        se
        m
        e   s
    e   s
'''