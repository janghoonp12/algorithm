N = int(input())
if N == 1:
    print(0)
    quit()
A = int(input())
inp = [int(input()) for i in range(N - 1)]
arr = [0] * (max(inp) + 1)

for i in inp:
    arr[i] += 1

ind = len(arr) - 1

ans = 0
while A <= ind:
    if arr[ind]:
        arr[ind] -= 1
        arr[ind - 1] += 1
        A += 1
        ans += 1
    else:
        ind -= 1
print(ans)