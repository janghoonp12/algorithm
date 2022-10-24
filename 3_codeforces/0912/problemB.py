from sys import stdin
input = stdin.readline

for q in range(int(input())):
    n = int(input())
    t = input()[:-1]
    s = ''
    i = n - 1
    while i >= 0:
        if t[i] != '0':
            s = chr(96 + int(t[i])) + s
            i -= 1
        else:
            s = chr(96 + int(t[i - 2] + t[i - 1])) + s
            i -= 3
    print(s)