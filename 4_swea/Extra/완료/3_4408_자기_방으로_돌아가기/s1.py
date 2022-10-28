# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    room = [0]*401
    m = 0
    for i in arr:
        if i[0] < i[1]:
            s = i[0]
            e = i[1]
        else:
            s = i[1]
            e = i[0]
        if s%2 == 0:
            s -= 1
        for j in range(s, e+1):
            room[j] += 1
            
    for i in room:
        if i > m:
            m = i
    print(f'#{t} {m}')