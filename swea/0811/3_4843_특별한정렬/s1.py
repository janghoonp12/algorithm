# import sys
# sys.stdin = open('input.txt', 'r')

def max_index(li):
    m = li[0]
    max_i = 0
    for i in range(len(li)):
        if li[i] > m:
            m = li[i]
            max_i = i
    return max_i

def min_index(li):
    m = li[0]
    min_i = 0
    for i in range(len(li)):
        if li[i] < m:
            m = li[i]
            min_i = i
    return min_i

def special_sort(arr):
    for i in range(10):
        if i%2:
            m = i + min_index(arr[i:])
            arr[i], arr[m] = arr[m], arr[i]
        else:
            m = i + max_index(arr[i:])
            arr[i], arr[m] = arr[m], arr[i]
    return arr


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = special_sort(arr)
    
    print(f'#{t}', end=' ')
    print(*arr[:10])