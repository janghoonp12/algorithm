a,b,c,d,e,f = map(int, input().split())
br = 0
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x+b*y == c:
            if d*x+e*y == f:
                br=1
                print(x,y)
                break
    if br==1: break
