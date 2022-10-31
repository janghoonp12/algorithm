def palindrome(s, e):
    while s < e:
        if S[s] == S[e]:
            s += 1
            e -= 1
            continue
        return False
    return True


S = ' ' + input()
arr = [float('INF') for i in range(len(S))]
arr[0] = 0
arr[1] = 1
for i in range(2, len(S)):
    for j in range(1, i + 1):
        if palindrome(j, i):
            arr[i] = min(arr[i], arr[j - 1] + 1)
print(arr)