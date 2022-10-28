# import sys
# sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    N, M = input().split()
    N = int(N)
    stack = [-1]*N
    top = -1
    for i in range(N):
        if M[i] == stack[top]:
            top -= 1
        else:
            top += 1
            stack[top] = M[i]
    ans = ''
    for i in stack[:top+1]:
        ans += i
    
    print(f'#{t}', ans)