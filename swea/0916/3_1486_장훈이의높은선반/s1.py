# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    
    
    ans = 0
    
    print(f'#{t}', ans)