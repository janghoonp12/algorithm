from sys import stdin
input = stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split())) + [0]

if sum(arr) < S:
    print(0)
    quit()

s = 0
e = 0
p_sum = arr[e]
ans = N

while e < N:
    if p_sum < S:
        e += 1
        p_sum += arr[e]
    else:
        ans = min(ans, e - s + 1)
        p_sum -= arr[s]
        s += 1

print(ans)