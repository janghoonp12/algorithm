# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    ans = 'Possible'
    for i in range(N):
        if (arr[i] // M) * K < i + 1:
            ans = 'Impossible'
            break

    print(f'#{t} {ans}')