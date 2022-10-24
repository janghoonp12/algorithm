from sys import stdin
input = stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    suffix = [0] * (n + 1)
    for i in range(1, n + 1):
        suffix[i] = arr[i] + suffix[i - 1]
    suffix = suffix[::-1]
    S = suffix[0]
    new = [0] * (n + 1)
    for i in range(n + 1):
        new[i] = suffix[0] - suffix[i]
    
    s = 1
    ans = n
    while s < n:
        if S % new[s]:
            s += 1
        else:
            temp = new[s]
            temp_idx = s
            tl = s
            for i in range(2, S // temp + 1):
                if i * temp not in new:
                    break
                else:
                    idx = new.index(i * temp)
                    tl = max(tl, idx - temp_idx)
                    temp_idx = idx
            else:
                ans = min(ans, tl)
            s += 1
    print(ans)