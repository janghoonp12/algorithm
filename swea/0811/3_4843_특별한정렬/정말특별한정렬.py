# import sys
# sys.stdin = open('input.txt', 'r')

'''
문제를 잘못 읽어서 정말 특별한 정렬을 만들었음...
큰1 작1 큰2 작2 큰3 작3 ... 정렬
'''

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

def special_sort(arr, N):
    count = 0
    for i in range(N):
        if count == N-1:
            break
        
        min_max = i%2
        num_sort = i//2 + 1
        
        if min_max == 0:
            for _ in range(num_sort):
                m = count + max_index(arr[count:])
                arr[count], arr[m] = arr[m], arr[count]
                count += 1
                if count == N-1:
                    break
                
        else:
            for _ in range(num_sort):
                m = count + min_index(arr[count:])
                arr[count], arr[m] = arr[m], arr[count]
                count += 1
                if count == N-1:
                    break
    return arr


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = special_sort(arr, N)
    
    print(f'#{t}', end=' ')
    print(*arr)