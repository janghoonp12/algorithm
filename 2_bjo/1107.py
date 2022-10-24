def recur(cur, num):
    global ans

    if cur == len(N) +1:
        ans = min(ans, cur + abs(num - n))
        return
    if cur:
        ans = min(ans, cur + abs(num - n))
    for i in range(10):
        if i in broken:
            continue
        recur(cur + 1, num * 10 + i)


N = input()
M = int(input())

n = int(N)
if n in (98, 99, 100, 101, 102, 103) or M == 10:
    print(abs(n - 100))
    quit()
elif M == 0:
    print(len(N))
    quit()

broken = tuple(map(int, input().split()))
ans = abs(n - 100)

recur(0, 0)

print(ans)