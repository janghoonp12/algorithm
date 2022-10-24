import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    t = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    M = 0
    s3 = s4 = 0
    for i in range(100):
        s1 = s2 = 0
        for j in range(100):
            s1 += arr[i][j]
            s2 += arr[j][i]
        s3 += arr[i][i]
        s4 += arr[99-i][i]
        
        if s1 > M:
            M = s1
        if s2 > M:
            M = s2
    if s3 > M:
        M = s3
    if s4 > M:
        M = s4        
    print(f'#{t} {M}')