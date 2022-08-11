import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    t = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    for i in range(102):
        if arr[99][i] == 2:
            X = i
    Y = 99
    
    while True:
        if Y == 0:
            break
        if arr[Y][X+1] == 1:
            while arr[Y][X+1] == 1:
                X += 1                 
        elif arr[Y][X-1] == 1:
            while arr[Y][X-1]:
                X -= 1
        Y -= 1
    
    print(f'#{t} {X-1}')