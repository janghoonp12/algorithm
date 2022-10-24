def recur(cur, start):
    global v_count
    
    if cur == L:
        if 1 <= v_count <= L - 2:
            for i in range(L):
                print(arr[i], end = '')
            print()
        return
    
    for i in range(start, C):
        temp = v_count
        if w_arr[i] in 'aeiou':
            v_count += 1
        arr[cur] = w_arr[i]
        recur(cur + 1, i + 1)
        v_count = temp


L, C = map(int, input().split())
w_arr = sorted(list(input().split()))
arr = [0 for i in range(L)]
v_count = 0

recur(0, 0)