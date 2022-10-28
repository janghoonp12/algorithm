n = int(input())
list = [list(map(int, input().split())) for i in range(n)]
area = 0


for j in range(100):
    for k in range(100):
        for l in range(n):
            if j>=list[l][0]:
                if j<list[l][0]+10:
                    if k>=list[l][1]:
                        if k<list[l][1]+10:
                            area +=1
                            break
print(area)
