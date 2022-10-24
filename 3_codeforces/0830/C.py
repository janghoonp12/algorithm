t = int(input())
for _ in range(t):
    n = int(input())
    dic = {}
    point = [0, 0, 0]
    for i in range(3):
        arr = list(input().split())
        for j in arr:
            dic[j] = dic.get(j, [0, 0, 0])
            dic[j][i] += 1
    for i in dic.values():
        if sum(i) == 1:
            for j in range(3):
                if i[j]:
                    point[j] += 3
        elif sum(i) == 2:
            for j in range(3):
                if i[j]:
                    point[j] += 1
    print(*point)