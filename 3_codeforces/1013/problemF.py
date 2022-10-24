from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    s = ['a']
    t = ['a']
    for _ in range(int(input())):
        d, k, x = input().split()
        if d == '1':
            s += list(x) * int(k)
            s.sort()
        else:
            t += list(x) * int(k)
            t.sort(reverse=True)
        
        if s < t:
            print('YES')
        else:
            print('NO')