def recur(cur):
    if cur == N - 1:
        E = A[0]
        for i in range(1, N):
            if arr[i-1] == '+':
                E += A[i]
            if arr[i-1] == '-':
                E -= A[i]
            if arr[i-1] == '*':
                E *= A[i]
            if arr[i-1] == '/':
                s = 1
                if E * A[i] < 0:
                    s = -1
                E = s * (abs(E) // abs(A[i]))
        ans.append(E)
        return

    for i in range(N - 1):
        if visited[i]:
            continue

        visited[i] = True
        arr[cur] = r[i]
        recur(cur + 1)
        visited[i] = False


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

R = '+-*/'
r = ''
for i in range(4):
    r += R[i] * B[i]

ans = []
arr = [0 for i in range(N - 1)]
visited = [False for i in range(N - 1)]
recur(0)
ans.sort()

print(ans[-1])
print(ans[0])