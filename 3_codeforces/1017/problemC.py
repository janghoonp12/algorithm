import sys
input = sys.stdin.readline


for t in range(int(input())):
    n = int(input())
    lid = '0' + input() + '0'
    arr = [0] + list(map(int, input().split())) + [0]

    s = e = 1
    ans = 0
    temp = []
    while e < n + 2:
        if lid[e] == '1':
            e += 1
        elif e == s:
                e += 1
                s += 1
        else:
            temp = sorted(arr[s - 1:e])
            ans += sum(temp) - temp[0]
            e += 1
            s = e
            
    print(ans)
        