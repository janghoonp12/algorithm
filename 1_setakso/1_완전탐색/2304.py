N = int(input())
li = []
for i in range(N):
    li.append(list(map(int, input().split())))

area = 0

for j in range(1001):
    L = []
    for k in li:
        if k[1] > j:
            L.append(k[0])
    if not L:
        break    
    area += (max(L) + 1) - min(L)
        
print(area)