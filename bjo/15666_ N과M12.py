from sys import stdin
I = stdin.readline

def recur(cur, start):
    if cur == M:
        print(*arr)
        return
    
    for i in range(start, len(n_arr)):
        arr[cur] = n_arr[i]
        recur(cur + 1, i)


N, M = map(int, I().split())
n_arr = sorted(list(set(map(int, I().split()))))
arr = [0] * M

recur(0, 0)
