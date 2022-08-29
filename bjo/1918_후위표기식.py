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



E = input()
ans = back_eq(E)

print(ans)