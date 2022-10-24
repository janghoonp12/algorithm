t = int(input())
for _ in range(t):
    N = input()
    s = 0
    for i in range(3):
        s += int(N[i]) - int(N[i+3])
    if s:
        print('NO')
    else:
        print('YES')
