def recur(cur, sum):
    if cur == N:
        if sum <= 1<<20:
            numbers[sum] += 1
        return
    
    recur(cur + 1, sum + S_arr[cur])
    recur(cur + 1, sum)


N = int(input())
S_arr = list(map(int, input().split()))

numbers = [0] * (1<<20 + 1)

recur(0, 0)

for i in range(1<<20 + 1):
    if not numbers[i]:
        print(i)
        quit()