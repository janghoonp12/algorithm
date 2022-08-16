import sys
sys.stdin = open('input.txt', 'r')

def is_pel(x):
    for i in range(len(x)//2):
        if x[i] != x[-1-i]:
            return False
    return True

for _ in range(10):
    t = int(input())
    arr = [input() for _ in range(100)]
    spin_arr = [[arr[j][i] for j in range(100)] for i in range(100)]

    ans = 0
    for i in range(100-ans):
        for j in range(100-ans):
            for k in range(100-ans):
                w = arr[i][j:100 - k]
                if is_pel(w):
                    if len(w) > ans:
                        ans = len(w)

                w = spin_arr[i][j:100 - k]
                if is_pel(w):
                    if len(w) > ans:
                        ans = len(w)
    
    print(f'#{t} {ans}')