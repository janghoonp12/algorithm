# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    pascal = [[1]]
    for i in range(N-1):
        arr = [1]+[pascal[i][j] + pascal[i][j+1] for j in range(i)] + [1]
        pascal.append(arr)
    
    print(f'#{t}')
    for i in pascal:
        print(*i)