# import sys
# sys.stdin = open('input.txt', 'r')

def count_sub(n):
    global ans
    
    if n:
        ans += 1
    if arr[n]:
        count_sub(arr[n][0])
        count_sub(arr[n][1])


T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    tree_path = list(map(int, input().split()))
    arr = [0 for i in range(E + 2)]
    
    for i in range(E):
        p = tree_path[2 * i]
        c = tree_path[2 * i + 1]
        if not arr[p]:
            arr[p] = [c, 0]
        else:
            arr[p][1] = c
    ans = 0
    
    count_sub(N)
    
    print(f'#{t}', ans)