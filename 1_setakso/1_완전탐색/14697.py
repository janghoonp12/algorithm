a,b,c,n = map(int, input().split())
pr = 0
for i in range(n+1):
    for j in range(n-i+1):
        for k in range(n-i-j+1):
            if a*i + b*j + c*k == n:
                pr = 1
                break
        if pr == 1: break
    if pr == 1: break
print(pr)
