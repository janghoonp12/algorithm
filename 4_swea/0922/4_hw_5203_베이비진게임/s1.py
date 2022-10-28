def babygin(li, c):
    if li[c] == 3:
        return True
    for i in range(3):
        count = 0
        for j in range(3):
            if li[c-2 + i + j]:
                count += 1
        if count == 3:
            return True
    return False


T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    p1 = p2 = False
    ans = 0
    arr1 = [0] * 14
    arr2 = [0] * 14
    for i in range(12):
        c = arr[i] + 2
        if not i % 2:
            arr1[c] += 1
            if babygin(arr1, c):
                p1 = True
        else:
            arr2[c] += 1
            if babygin(arr2, c):
                p2 = True
        if p1 or p2:
            break
    if p1:
        ans = 1
    elif p2:
        ans = 2
    print(f'#{t}', ans)