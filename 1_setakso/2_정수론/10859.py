n = int(input())
if n == 1:
    print('no')
    quit()

def dpr(x):
    val = 0
    i = 2
    while i**2<=x:
        if x%i==0:
            val = 1
            break
        i+=1
    return val


ch = 1
A = [0,1,2,5,8]
B = [6,9]
C = [3,4,7]
m=0
t=n
i=0


while t!=0:
    if t%10 in C:
        ch = 0
        break
    elif t%10 in A:
        m = 10*m + t%10
    elif t%10 in B:
        if t%10==6:
            m = 10*m + 9
        else:
            m = 10*m + 6
    t//=10
    i+=1

if ch == 0:
    print('no')
elif dpr(n)==1:
    print('no')
elif dpr(m)==1:
    print('no')
else:
    print('yes')
