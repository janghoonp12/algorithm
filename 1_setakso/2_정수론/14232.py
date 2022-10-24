def divi(i):
    li=[]
    n=2
    x=i
    while n<=(i**(1/2)):
        while x%n==0:
            x//=n
            li.append(n)
        n+=1
    if x>=(i**(1/2)):
        li.append(x)
    return(li)

k = int(input())

liss=divi(k)

print(len(liss))
print(*liss)
