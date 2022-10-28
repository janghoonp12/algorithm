a,b,c,d,e = map(int, input().split())
for i in range(1, 1000001):
    count = 0
    if i%a == 0:
        count+=1
    if i%b == 0:
        count+=1
    if i%c == 0:
        count+=1
    if i%d == 0:
        count+=1
    if i%e == 0:
        count+=1
    if count>=3:
        print(i)
        break
