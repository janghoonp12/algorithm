# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    M = m = arr[0]
    for j in range(N):
        n = arr[j]
        if n > M:
            M = n
        elif n < m:
            m = n
    print(f'#{i} {M - m}')
