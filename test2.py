n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

print(arr)
for i in range(n-2, -1, -1):
    for j in range(i):
        arr[i][j] += max(arr[i + 1][j], arr[i + 1][j + 1])
    
print(arr[0][0])