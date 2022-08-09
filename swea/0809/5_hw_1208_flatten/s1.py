import sys
sys.stdin = open('input.txt', 'r')

def count(li):
    C = [0]*101
    for i in li:
        C[i] += 1
    return C

for t in range(1, 11):
    D = int(input())
    arr = list(map(int, input().split()))
    li = count(arr)

    s = 0
    num_l = 0
    while num_l <= D:
        if li[s] != 0:
            num_l += li[s]
            li[s+1] += li[s]
            li[s] = 0
            m = s
        s += 1
    e = 100
    num_u = 0
    while num_u <= D:
        if li[e] != 0:
            num_u += li[e]
            li[e-1] += li[e]
            li[e] = 0
            M = e
        e -= 1
    print(f'#{t} {M-m}')