import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    li = [0]*5001
    
    N = int(input())
    for i in range(1, N+1):
        A, B = (map(int, input().split()))
        for j in range(A, B+1):
            li[j] += 1
    
    P = int(input())
    ans = ''
    for j in range(1, P+1):
        ans += str(li[int(input())]) + ' '
        
    print(f'#{t} {ans}')
    