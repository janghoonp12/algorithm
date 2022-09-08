def recur(cur, prot, fat, carb, vit, price):
    global ans, food

    if cur == N:
        if prot >= nutri[0] and fat >= nutri[1] and carb >= nutri[2] and vit >= nutri[3]:
            if price < ans:
                ans = price
                food = [f_arr[:]]
            elif price == ans:
                food.append(f_arr[:])

        return
    
    f_arr.append(cur + 1)
    recur(cur + 1, prot + arr[cur][0], fat + arr[cur][1], carb + arr[cur][2], vit + arr[cur][3], price + arr[cur][4])
    f_arr.pop()
    recur(cur + 1, prot, fat, carb, vit, price)

N = int(input())
nutri = tuple(map(int, input().split())) 
arr = [tuple(map(int, input().split())) for i in range(N)]
ans = 10000
f_arr = []
food = []

recur(0, 0, 0, 0, 0, 0)

if ans == 10000:
    print(-1)
else:
    print(ans)
    print(*sorted(food)[0])