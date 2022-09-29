# import sys
# sys.stdin = open('input.txt', 'r')

def heap(i):
    if i > 0:
        if tree_value[i] < tree_value[i//2]:
            tree_value[i], tree_value[i//2] = tree_value[i//2], tree_value[i]
            heap(i // 2)

T = int(input())
for t in range(1, T+1):
    
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    
    tree_value = [0] * (N + 1)
    
    for i in range(1, N + 1):
        tree_value[i] = arr[i]
        heap(i)

    ans = 0
    while N > 0:
        N //= 2
        ans += tree_value[N]
    
    print(f'#{t}', ans)