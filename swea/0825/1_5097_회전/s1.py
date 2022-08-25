# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    
    for i in range(M):
        queue.append(queue.pop(0))
    ans = queue[0]
    
    print(f'#{t} {ans}')