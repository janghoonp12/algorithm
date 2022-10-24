def recur(cur):
    global fin

    if fin:
        return

    for i in range(cur // 2):
        if arr[cur - 2 * (i + 1) : cur - (i + 1)] == arr[cur - (i + 1) : cur]:
            return

    if cur == N:
        for i in arr:
            print(i, end = '')
        fin = True
        return

    for i in range(3):
        arr[cur] = i + 1
        recur(cur + 1)

N = int(input())
arr = [0 for i in range(N)]
fin = False

recur(0)