# import sys
# sys.stdin = open('input.txt', 'r')

def my_eval(equation):
    stack = []
    for char in equation:
        if char in'*/+-':
            x = stack.pop()
            y = stack.pop()
            if char == '+':
                stack.append(y+x)
            if char == '-':
                stack.append(y-x)
            if char == '*':
                stack.append(y*x)
            if char == '/':
                stack.append(y/x)
        else:
            stack.append(int(char))
    return stack[-1]

str1 = input()
stack = []
result = ''

for char in str1:
    if char in '*/+-()':
        if not stack:
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char in '*/':
            while stack and stack[-1] in '*/':
                result += stack.pop()
            stack.append(char)
        elif char in '+-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(char)
        else:
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()        
    else:
        result += char

while stack:
    result += stack.pop()

print(result)
print(my_eval(result))