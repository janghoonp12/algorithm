# import sys
# sys.stdin = open('input.txt', 'r')

def find_value(n):
    if n > N:
        return
    
    find_value(2 * n)
    find_value(2 * n + 1)
    arr[n // 2] += arr[n]

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0] * (N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        arr[a] = b
        
    find_value(L)
    
    print(f'#{t}', arr[L])