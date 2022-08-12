# import sys
# sys.stdin = open('input.txt', 'r')

def my_min(a, b):
    if a > b:
        return b
    else:
        return a

def multisum(A, B):
    s = 0
    for i in range(len(A)):
        s += A[i] * B[i]
    return s

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    ans = -1<<60
    if N < M:
        for i in range(M-N+1):
            s = multisum(A, B[i:i+N])
            if s > ans:
                ans = s
    else:
        for i in range(N-M+1):
            s = multisum(A[i:i+M], B)
            if s > ans:
                ans = s

    print(f'#{t} {ans}')