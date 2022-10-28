from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    n, q = map(int, input().split())
    steps = [0] + list(map(int, input().split()))
    question = list(map(int, input().split()))
    temp = [(0, 1)]
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        if steps[i] > temp[-1][0]:
            temp.append((steps[i], i))
        prefix[i] = steps[i] + prefix[i - 1]
    temp.append((float('INF'), n + 1))
    for i in range(q):
        s = 0
        e = t = len(temp) - 1
        while s <= e:
            m = (s + e) // 2
            if temp[m][0] <= question[i]:
                s = m + 1
            else:
                e = m - 1
                t = m
        print(prefix[temp[t][1] - 1], end=' ')
    print()