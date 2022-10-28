from sys import stdin
input = stdin.readline

for t in range(int(input())):
    a, b, c = map(int, input().split())
    n1 = abs(a - 1)
    n2 = abs(b - c) + abs(c - 1)
    
    if n1 == n2:
        print(3)
    elif n1 < n2:
        print(1)
    else:
        print(2)