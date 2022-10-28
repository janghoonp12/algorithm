T = int(input())
for t in range(1, T+1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    for i in range(12):
        plan[i] = min(price[0]*plan[i], price[1])

    m = price[3]
    i = 0
    visited = [0]*14
    while True:
        if i >= 12:
            i -= 1
            s = 0
            count_3 = 0
            for j in range(14):
                if visited[j] == 1:
                    s += plan[j]
                elif visited[j] == 3:
                    count_3 += 1
            s += price[2]*count_3//3
            m = min(m, s)

            while visited[i] != 3 and i > -2:
                i -= 1
            if i == -2:
                break
            else:
                for j in range(2):
                    visited[i] = 0
                    i -= 1
                visited[i] = 1
                i += 1

        elif plan[i] == 0:
            i += 1
        else:
            for j in range(3):
                visited[i] = 3
                i += 1
    
    print(f'#{t}', m)