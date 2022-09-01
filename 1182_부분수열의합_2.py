from sys import stdin
input = stdin.readline

def recur(cur, sub) :
    global cnt
    if cur == N:
        if sub == S:
            cnt += 1
        return

    recur(cur + 1, sub + arr[cur])
    recur(cur + 1, sub)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

recur(0, 0)

if not S:
    cnt -= 1

print(cnt)