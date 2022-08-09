from sys import stdin, stdout
I = stdin.readline
P = stdout.write

T = int(I())
for i in range(T):
    k, n = map(int, I().split())
    C1 = list(map(int, I().split()))
    C2 = list(map(int, I().split()))
    C3 = list(map(int, I().split()))
    C4 = list(map(int, I().split()))
    C1.sort()
    C2.sort()
    C3.sort()
    C4.sort()
    s = [0, 0, 0, 0]
    e = [n, n, n, n]

    for a in range(s[0], e[0]):
        for b in range(s[1], e[1]):
            for c in range(s[2], e[2]):
                for d in range(s[3], e[3]):
                    S = C1[a] + C2[b] + C3[c] + C4[d]
                    if S > k:
                        e[0] = a + 1
                        e[1] = b + 1
                        e[2] = c + 1
                        e[3] = d + 1
                    elif S < k:
                        s[0] = a
                        s[1] = b
                        s[2] = c
                        s[3] = d
                    print(S)
                    


'''
k = 300, n = 4

40 52 60 80     63 68 75 88     48 48 54 93     49 56 73 75
i  x  x  x         j  x  x            k  x            l  x

S = i + j + k + l

1. S > k: 뒤에 있는 수들은 확인 할 필요 없음.
2. S < k: 앞에 있는 수들은 확인 할 필요 없음.



''' 