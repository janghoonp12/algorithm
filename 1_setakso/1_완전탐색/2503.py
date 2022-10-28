n = int(input())
lt = []
ans = 0
for i in range(n):
    lt.append(list(input().split()))

for j in range(1, 10):
    for k in range(1, 10):
        if k == j:
            continue
        for l in range(1, 10):
            if l == j:
                continue
            elif l == k:
                continue
            else:
                count = 0
                for m in range(n):
                    spl = list(lt[m][0])
                    st = int(lt[m][1])
                    ba = int(lt[m][2])
                    s = 0
                    b = 0
                    if str(j) in spl:
                        b = b+1
                        if str(j)==spl[0]:
                            s = s+1
                            b = b-1
                    if str(k) in spl:
                        b = b+1
                        if str(k)==spl[1]:
                            s = s+1
                            b = b-1
                    if str(l) in spl:
                        b = b+1
                        if str(l)==spl[2]:
                            s = s+1
                            b = b-1
                    if s == st:
                        if b == ba:
                            count = count+1
                    if count == n:
                        ans = ans+1
print(ans)
