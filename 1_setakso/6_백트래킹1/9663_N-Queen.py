def recur(cur):
    global ans

    if cur == N:
        ans += 1
        return

    for i in range(N):
        if i in arr[:cur]:
            continue

        for j in range(cur):
            if arr[cur - (j + 1)] == i + (j + 1) or arr[cur - (j + 1)] == i - (j + 1):
                break
        else:
            arr[cur] = i
            recur(cur + 1)


N = int(input())
arr = [0 for i in range(N)]
ans = 0
recur(0)

print(ans)