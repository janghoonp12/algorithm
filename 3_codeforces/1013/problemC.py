R = 'RRRRRRRR'
BB = ['B'] * 8
temp = [0] * 8
for _ in range(int(input())):
    input()
    arr = [input() for i in range(8)]
    if R in arr:
        print('R')
    else:
        for j in range(8):
            for i in range(8):
                temp[i] = arr[i][j]
            if temp == BB:
                print('B')
                break