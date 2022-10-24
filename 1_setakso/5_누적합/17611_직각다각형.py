from sys import stdin
I = stdin.readline

n = int(I())
arr = [list(map(int, I().split())) for _ in range(n)]
arr.append(arr[0])

arr_X = [0]*1000003
arr_Y = [0]*1000003

for i in range(n):
    arr_X[min(arr[i][0], arr[i+1][0]) + 500001] += 1
    arr_X[max(arr[i][0], arr[i+1][0]) + 500001] -= 1
    arr_Y[min(arr[i][1], arr[i+1][1]) + 500001] += 1
    arr_Y[max(arr[i][1], arr[i+1][1]) + 500001] -= 1

prefix_X = [0]*1000003
prefix_Y = [0]*1000003

for i in range(1, 1000003):
    prefix_X[i] = arr_X[i] + prefix_X[i-1]
    prefix_Y[i] = arr_Y[i] + prefix_Y[i-1]

print(max(max(prefix_X), max(prefix_Y)))