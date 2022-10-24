for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    m = 10 - n
    ans = m * (m - 1) // 2 * 6
    print(ans)