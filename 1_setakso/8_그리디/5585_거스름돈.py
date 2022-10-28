N = int(input())

cash = [500, 100, 50, 10, 5, 1]
change = 1000 - N
ans = 0
for i in range(6):
    ans += change // cash[i]
    change %= cash[i]
    
print(ans)