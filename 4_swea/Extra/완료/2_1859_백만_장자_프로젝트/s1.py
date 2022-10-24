# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    i = N - 1
    p = arr[i]
    ans = 0
    while i >=0:
        if arr[i] <= p:
            ans += p - arr[i]
        else:
            p = arr[i]
        i -= 1
    print(f'#{t} {ans}')