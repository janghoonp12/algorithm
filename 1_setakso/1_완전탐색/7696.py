li=[]
count=0

for i in range(100000000):
    a = list(str(i))
    if len(set(a))==len(a):
        li.append(i)
        count = count+1
    if count == 1000001:
        break
print(li)

while True:
    b=int(input())
    if b!=0:
        print(li[b])
    else:
        break
