n, m, k = map(int, input().split())
for i in range(1, 101):
    if n-2*i<0:
        print(i-1)
        break
    elif m-i<0:
        print(i-1)
        break
    elif n-2*i+m-i<k:
        print(i-1)
        break
