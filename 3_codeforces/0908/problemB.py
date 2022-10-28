from sys import stdin
input = stdin.readline

arr = [[], [1], [1, 2], [2, 1, 3], [2, 1, 3, 4], [1, 2, 3, 4, 5], [2, 1, 4, 3, 5, 6], [1, 2, 3, 5, 4, 6, 7]] + [0] * 100
for i in range(8, 101):
    arr[i] = arr[i - 2][:-2] + [i - 2, i - 3, i - 1, i]

for t in range(int(input())):
    print(*arr[int(input())])
    
    