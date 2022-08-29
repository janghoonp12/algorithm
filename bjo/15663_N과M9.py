from sys import stdin, stdout
I = stdin.readline
P = stdout.write

def recur(cur):
    if cur == M:
        print(*arr)
        return

    for i in range(len(c_arr)):
        if c_arr[i][1] == 0:
            continue
        
        arr[cur] = c_arr[i][0]
        c_arr[i][1] -= 1
        recur(cur + 1)
        c_arr[i][1] += 1
        


N, M = map(int, I().split())
n_arr = sorted(list(map(int, I().split()))) + [0]
c_arr = []
s = 0
for i in range(0, N):
    s += 1
    if n_arr[i] != n_arr[i + 1]:
        c_arr.append([n_arr[i], s])
        s = 0

arr = [0] * M

recur(0)
