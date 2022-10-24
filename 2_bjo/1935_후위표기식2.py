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
            stack.append(arr[ord(i) - ord('A')])
    
    return stack[-1]



N = int(input())
E = input()
arr = [int(input()) for i in range(N)]

ans = my_eval(E)

print(f'{ans:.2f}')
