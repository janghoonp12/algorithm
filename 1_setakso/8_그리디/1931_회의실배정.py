from sys import stdin
input = stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
arr.sort(key=lambda x : (x[1], x[0]))
ans = 0
e = 0
for i in arr:
    if i[0] >= e:
        ans += 1
        e = i[1]
print(ans)