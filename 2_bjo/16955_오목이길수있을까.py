arr = [list(input()) for i in range(10)]

for i in range(10):
    for j in range(10):
        if arr[i][j] != '.':
            continue
        
        arr[i][j] = 'X'
        for x in range(10):
            for y in range(10):
                if arr[x][y] == 'X':
                    temp1 = 0
                    temp2 = 0
                    temp3 = 0
                    temp4 = 0
                    for z in range(5):
                        if x + z == 10 or arr[x + z][y] != 'X':
                            break
                        temp1 += 1
                    for z in range(5):
                        if y + z == 10 or arr[x][y + z] != 'X':
                            break
                        temp2 += 1
                    for z in range(5):
                        if x + z == 10 or y + z == 10 or arr[x + z][y + z] != 'X':
                            break
                        temp3 += 1
                    for z in range(5):
                        if x + z == 10 or y - z == -1 or arr[x + z][y - z] != 'X':
                            break
                        temp4 += 1
                    if temp1 == 5 or temp2 == 5 or temp3 == 5 or temp4 == 5:
                        print(1)
                        quit()
        arr[i][j] = '.'
print(0)