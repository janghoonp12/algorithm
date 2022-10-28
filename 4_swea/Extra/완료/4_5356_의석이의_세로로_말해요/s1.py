# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    arr = [input() for _ in range(5)]

    n = 0
    for i in arr:
        if len(i) > n:
            n = len(i)
    
    ans = ''
    for i in range(n):
        for j in range(5):
            try:
                ans += arr[j][i]
            except:
                continue

    print(f'#{t} {ans}')