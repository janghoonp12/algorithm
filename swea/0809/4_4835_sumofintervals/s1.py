# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    s = 0
    e = 0
    partial_sum = 0
    for i in range(M):
        partial_sum += arr[i]
        e = i
    M = m = partial_sum
    while e < N - 1:
        e += 1
        partial_sum += arr[e]
        partial_sum -= arr[s]
        s += 1
        if partial_sum > M:
            M = partial_sum
        elif partial_sum < m:
            m = partial_sum
    print(f'#{t} {M - m}')
