from sys import stdin
input = stdin.readline


def recur(arr):
    global ans, fin
    if fin:
        return
    if len(arr) == 1:
        return
    
    A = arr[:len(arr) // 2]
    B = arr[len(arr) // 2:]
    a1 = min(A)
    a2 = max(A)
    b1 = min(B)
    b2 = max(B)
    
    if a1 == 1 and a2 == len(arr) // 2:
        recur(A)
        for i in range(len(B)):
            B[i] = B[i] - b1 + 1
        recur(B)
    
    elif b1 == 1 and b2 == len(arr) // 2:
        ans += 1
        for i in range(len(A)):
            A[i] = A[i] - a1 + 1
        recur(A)
        recur(B)
    
    else:
        fin = True
        return
    

t = int(input())
for _ in range(t):
    m = int(input())
    P = list(map(int, input().split()))
    ans = 0
    fin = False
    recur(P)
    
    if fin:
        print(-1)
    else:
        print(ans)