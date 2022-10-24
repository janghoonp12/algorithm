a, b, n, w = map(int, input().split())
count = 0
s = 0
g = 0
for i in range(1, n):
    if a*i + b*(n-i) == w:
        count += 1
        s = i
        g = n-i
if count == 1:
    print(s, g, count)
else:
    print("-1")
