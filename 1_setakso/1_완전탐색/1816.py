n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
for j in range(n):
    p = 0
    for k in range(2,1000001):
        if num[j]%k == 0:
            print("NO")
            p = 1
            break
    if p == 0:
        print("YES")
