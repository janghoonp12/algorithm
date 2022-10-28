from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    a, b = input().split()
    if a[-1] == 'S':
        if b[-1] == 'S':
            if len(a) < len(b):
                print('>')
            elif len(a) == len(b):
                print('=')
            else:
                print('<')
        else:
            print('<')
    elif a[-1] == 'M':
        if b[-1] == 'S':
            print('>')
        elif b[-1] == 'M':
            print('=')
        else:
            print('<')
    else:
        if b[-1] == 'L':
            if len(a) < len(b):
                print('<')
            elif len(a) == len(b):
                print('=')
            else:
                print('>')
        else:
            print('>') 