a, d = map(int, input().split())
q = int(input())

def gcdt(x,y):
    while x%y != 0:
        g = x%y
        x = y
        y = g
    return y

A = []
for j in range(10**6+10):
    A.append(a+(j-1)*d)

for i in range(q):
    t, l, r = map(int, input().split())
    if t == 1:
        ans = (A[l] + A[r])*(r-l+1)//2
    elif l==r:
        ans = A[l]
    else:
        ans = gcdt(A[l],d)
    print(ans)
