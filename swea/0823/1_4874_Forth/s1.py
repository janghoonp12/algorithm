# import sys
# sys.stdin = open('input.txt', 'r')

def my_eval(eq):
    stack = []
    for i in eq:
        if i == '.':
            if len(stack) == 1:
                return stack[-1]
            else:
                1/0
        elif i in '*/+-':
            y = stack.pop()
            x = stack.pop()
            if i == '+':
                stack.append(x + y)
            elif i == '-':
                stack.append(x - y)
            elif i == '*':
                stack.append(x * y)
            elif i == '/':
                stack.append(x // y)
        else:
            stack.append(int(i))


T = int(input())
for t in range(1, T+1):
    E = input().split()
    try :
        ans = my_eval(E)
    except:
        ans = 'error'
    
    print(f'#{t} {ans}')