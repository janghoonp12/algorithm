def recur(cur, work, pay, temp):
    global ans

    if cur == N:
        if work:
            ans = max(ans, pay - temp)
        else:
            ans = max(ans, pay)
        return

    if work:
        recur(cur + 1, work - 1, pay, temp)
    else:
        recur(cur + 1, arr[cur][0] - 1, pay + arr[cur][1], arr[cur][1])
        recur(cur + 1, work, pay, 0)


N = int(input())
arr = [tuple(map(int, input().split())) for i in range(N)]
ans = 0

recur(0, 0, 0, 0)

print(ans)