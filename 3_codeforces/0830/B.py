t = int(input())
for _ in range(t):
    N = int(input())
    A = list(input())
    B = list(input())
    for i in range(N):
        if A[i] == B[i]:
            continue
        elif A[i] == 'G' and B[i] == 'B':
            continue
        elif A[i] == 'B' and B[i] == 'G':
            continue
        else:
            break
    else:
        print('YES')
        continue
    print('NO')