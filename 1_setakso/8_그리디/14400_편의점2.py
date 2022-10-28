from sys import stdin
input = stdin.readline

n = int(input())
arr_x = []
arr_y = []
for i in range(n):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)
arr_x.sort()
arr_y.sort()
X = arr_x[n // 2]
Y = arr_y[n // 2]
ans = 0
for i in range(n):
    ans += abs(arr_x[i] - X) + abs(arr_y[i] - Y)
print(ans)