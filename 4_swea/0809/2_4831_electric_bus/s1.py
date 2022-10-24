# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.append(N + 1)
    b = 0
    c = 0
    count = 0
    while b + K < N:
        if arr[c] <= b + K:
            c += 1
        elif c == 0 or arr[c - 1] == b:
            count = 0
            break
        else:
            b = arr[c - 1]
            count += 1 
    print(f'#{i} {count}')
