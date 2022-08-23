# import sys
# sys.stdin = open('input.txt', 'r')

def back_eq(eq):
    stack = []
    result = ''
    for i in eq:
        if i in '*/+-()':
            if i == '(':
                stack.append(i)
            elif i in '*/':
                while stack and stack[-1] in '*/':
                    result += stack.pop()
                stack.append(i)
            elif i in '+-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(i)
            else:
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
        else:
            result += i
    
    while stack:
        result += stack.pop()
    
    return result


def my_eval(eq):
    stack = []
    for i in eq:
        if i in '*/+-':
            y = stack.pop()
            x = stack.pop()
            if i == '+':
                stack.append(x + y)
            if i == '-':
                stack.append(x - y)
            if i == '*':
                stack.append(x * y)
            if i == '/':
                stack.append(x / y)
        else:
            stack.append(int(i))
    
    return stack[-1]


T = 10
for t in range(1, T+1):
    N = int(input())
    E = input()

    B = back_eq(E)
    ans = my_eval(B)

    print(f'#{t} {ans}')