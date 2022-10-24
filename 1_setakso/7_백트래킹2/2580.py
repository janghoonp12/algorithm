from sys import stdin
I = stdin.readline

def check_sudoku(arr):
    for i in range(9):
        arr_r = [0]*10
        arr_c = [0]*10
        arr_b = [0]*10
        for j in range(9):
            arr_r[arr[i][j]] += 1
            arr_c[arr[j][i]] += 1
            arr_b[arr[3 * (i // 3) + j // 3][3 * (i % 3) + j % 3]] += 1
        for j in range(1,10):
            if not arr_r[j] or not arr_c[j] or not arr_b[j]:
                return False
    return True            
    
def recur(cur):
    if cur == len(empty):
        for i in arr:
            print(*i)
        print()
        if check_sudoku(arr):
            for i in arr:
                print(*i)
            quit()
        return
            
    for i in numbers:
        arr[empty[cur][0]][empty[cur][1]] = i
        recur(cur + 1)
    
    
arr = [list(map(int, I().split())) for i in range(9)]
empty = []

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            empty.append((i, j))

recur(0)