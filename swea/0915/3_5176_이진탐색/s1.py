# import sys
# sys.stdin = open('input.txt', 'r')

def find_value(n):
    global k
    
    if n <= N:    
        find_value(2 * n)
        tree[n] = k
        k += 1
        find_value(2 * n + 1)
    
    
T = int(input())
for t in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    k = 1
    
    find_value(1)
    
    print(f'#{t}', tree[1], tree[N//2])