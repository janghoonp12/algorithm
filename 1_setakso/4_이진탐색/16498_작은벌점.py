from sys import stdin
I = stdin.readline

a, b, c = map(int, I().split())
A = list(map(int, I().split()))
B = list(map(int, I().split()))
C = sorted(list(map(int, I().split())))
D = 200000000

for i in A:
    for j in B:
        M = max(i, j)
        m = min(i, j)
        
        if m > C[c-1]:
            d = M - C[c-1]
            print(f'case #1 m and M is {m}, {M}, C[c-1]is {C[c-1]}, so d is {d}')
        elif M < C[0]:
            d = C[0] - m
            print(f'case #2 m and M is {m}, {M}, C[0]is {C[0]}, so d is {d}')
        else:
            s = 0
            e = c - 1
            upper = 0
            while s <= e:
                mid = (s + e) // 2
                if C[mid] < m:
                    s = mid + 1
                else:
                    upper = mid
                    e = mid - 1

            s = 0
            e = c - 1
            lower = c - 1
            while s <= e:
                mid = (s + e) // 2
                if C[mid] > M:
                    e = mid - 1
                else:
                    lower = mid
                    s = mid + 1

            d = max(M - m, min(C[upper] - m, M - C[lower]))
            print(f'case #3 m and M is {m}, {M}, m upper is {C[upper]}, M lower is {C[lower]}, so d is {d}')
        if d < D:
            print(f'change {D} to {d}')
            D = d
print(D)
