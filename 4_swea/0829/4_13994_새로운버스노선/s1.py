# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    stop = [0]* 1001
    for i in range(N):
        P, A, B = map(int, input().split())
        stop[A] += 1
        stop[B] += 1
        if P == 1:
            for i in range(A + 1, B):
                stop[i] += 1
        elif P == 2:
            for i in range(A + 2, B, 2):
                stop[i] += 1
        else:
            if A % 2:
                for i in range(A + 1, B):
                    if not i % 3 and i % 10:
                        stop[i] += 1
            else:
                for i in range(A + 1, B):
                    if not i % 4:
                        stop[i] += 1
    
    ans = max(stop)
    
    print(f'#{t}', ans)
