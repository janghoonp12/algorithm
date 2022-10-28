a, d = map(int, input().split())
q = int(input())

def gcdt(x,y):
    while x%y != 0:
        g = x%y
        x = y
        y = g
    return y

def A(n):
    return a + (n-1)*d

alist = []

for i in range(q):
    t, l, r = map(int, input().split())
    if t == 1:
        ans = (A(l) + A(r))*(r-l+1)//2
    elif l==r:
        ans = A(l)
    else:
        ans = gcdt(A(l),d)
    alist.append(ans)

for i in range(q):
    print(alist[i])


'''
        a a+d a+2d a+3d a+4d a+5d a+6d ... a+nd
        0. l = r인 경우 A(l)이 최대공약수

        1. l < r이고 a와 d가 서로소인 경우
            a와 a+d는 서로소 => 최대공약수 1?
            a+ld a+(l+1)d

        2. d가 a와 최대공약수 c가 있는 경우(a=kc, d=jc)
            kc (k+j)c (k+2j)c (k+3j)c ... (k+nj)c
            c곱하기 k k+j k+2j k+3j ... k+nj 의 최대 공약수
            k와 j는 서로소 => 최대공약수 1
'''


'''
1 l r : A_l + A_(l+1) + ... + A_(r-1) + A_r
r-l+1항 : (A_r + A_l)/2 *(r-l+1)

2 l r : gcd(A_l, ... , A_r)
gcd(A_l, A_(l+1))



'''
