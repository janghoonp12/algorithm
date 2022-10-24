T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    if n == 1 and m == 1:
        print(0)
    else:
        print(n+m+min(n,m)-2)