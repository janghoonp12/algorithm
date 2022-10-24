from sys import stdin
input = stdin.readline


T = int(input())
for t in range(T):
    N = int(input())
    check = [0 for i in range(N + 1)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        check[b] = a
    n1, n2 = map(int, input().split())
    
    A1 = []
    A2 = []
    while n1:
        A1.append(n1)
        n1 = check[n1]
    while n2:
        A2.append(n2)
        n2 = check[n2]
    
    ans = 0
    for i in range(min(len(A1), len(A2))):
        if A1[-1 - i] == A2[-1 - i]:
            ans = A1[-1 - i]
        else:
            break
    print(ans)