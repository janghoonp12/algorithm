def count(arr, n):
    li = [False]*n
    s = 1
    num = 1
    for i in range(1, n):
        num += 1
        if arr[i] == arr[i-1]:
            li[i] = True
            num -= 1
        s += num
    return li, s
    

n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    i, x = map(int, input().split())
    arr[i-1] = x
    count_arr, count_sum = count(arr, n)
    S = count_sum
    for j in range(1, n):
        if count_arr[j]:
            count_sum -= 1
        else:
            count_sum -= n-j+1
        S += count_sum
    print(S)