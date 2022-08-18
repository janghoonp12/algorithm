# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    C = input()
    
    B = ['{', '(', '}', ')']
    stack = [0]*len(C)
    top = -1
    ans = 0

    for i in C:
        if i == B[2]:
            if stack[top] == B[0]:
                top -= 1
            else:
                top = 0
                break
        elif i == B[3]:
            if stack[top] == B[1]:
                top -= 1
            else:
                top = 0
                break
        elif i in B:
            top += 1
            stack[top] = i
    
    if top == -1:
        ans = 1

    print(f'#{t} {ans}')