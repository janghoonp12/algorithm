# import sys
# sys.stdin = open('input.txt', 'r')

def factor(N):
    li = [0]*5
    p = [2, 3, 5, 7, 11]
    for i in range(5):
        while N % p[i] == 0:
            li[i] += 1
            N //= p[i]
    st = ''
    for i in li:
        st += str(i) + ' '
    return st

T = int(input())
for t in range(1, T+1):
    N = int(input())
    print(f'#{t} {factor(N)}')