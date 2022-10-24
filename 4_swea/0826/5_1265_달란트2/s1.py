# import sys
# sys.stdin = open('input.txt', 'r')
def recur(cur, start):
    global ans
    if sum(arr[:cur]) >= N:
        return

    if cur == P - 1:
        arr[P - 1] = N - sum(arr[:P - 1])
        m = 1
        for i in arr:
            m *= i
        ans = max(ans, m)
        return
    
    for i in range(start, N - P + 2):
        arr[cur] = i
        recur(cur + 1, i)


T = int(input())
for t in range(1, T+1):
    N, P = map(int, input().split())
    arr = [0 for i in range(P)]
    ans = 0

    recur(0, 1)

    print(f'#{t}', ans)
