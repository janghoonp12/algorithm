# import sys
# sys.stdin = open('input.txt', 'r')

def itoa(N):
    if N < 0:
        N_str = '-'
        N = N * -1
    else:
        N_str = ''
    S = ''
    while N != 0:
        S += chr(N % 10 + ord('0'))
        N = N // 10
    for i in range(len(S)):
        N_str += S[-i-1]
    return N_str

T = int(input())
for t in range(1, T+1):
    N = int(input())
    new_N = itoa(N)
    print(f'#{t} {new_N} {type(new_N)}')