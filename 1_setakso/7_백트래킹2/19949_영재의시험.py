def recur(cur, correct):
    global count
    
    if cur > 2 and arr[cur - 1] == arr[cur - 2] and arr[cur - 2] == arr[cur - 3]:
        return
    
    if cur == 10:
        if correct >= 5:
            count += 1
        return
    
    for i in range(1, 6):
        arr[cur] = i
        if i == ans_sheet[cur]:
            recur(cur + 1, correct + 1)
        else:
            recur(cur + 1, correct)


ans_sheet = list(map(int, input().split()))
arr = [0] * 10
count = 0

recur(0, 0)

print(count)