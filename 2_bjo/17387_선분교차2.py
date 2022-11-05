x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

ans = 0
if x1 == x2:
    if x3 == x4:
        if x1 == x3:
            if min(y1, y2) <= y3 <= max(y1, y2) or min(y1, y2) <= y4 <= max(y1, y2) or min(y3, y4) <= y1 <= max(y3, y4) or min(y3, y4) <= y2 <= max(y3, y4):
                ans = 1
    elif y3 == y4:
        if min(y1, y2) <= y3 <= max(y1, y2) and min(x3, x4) <= x1 <= max(x3, x4):
            ans = 1
    else:
        if min(x3, x4) <= x1 <= max(x3, x4) and min(y1, y2) <= (y4 - y3) * (x1 - x3) / (x4 - x3) + y3 <= max(y1, y2):
            ans = 1
elif y1 == y2:
    if x3 == x4:
        if min(x1, x2) <= x3 <= max(x1, x2) and min(y3, y4) <= y1 <= max(y3, y4):
            ans = 1
    elif y3 == y4:
        if y1 == y3:
            if min(x1, x2) <= x3 <= max(x1, x2) or min(x1, x2) <= x4 <= max(x1, x2) or min(x3, x4) <= x1 <= max(x3, x4) or min(x3, x4) <= x2 <= max(x3, x4):
                ans = 1
    else:
        if min(y3, y4) <= y1 <= max(y3, y4) and min(x1, x2) <= (x4 - x3) * (y1 - y3) / (y4 - y3) + x3 <= max(x1, x2):
            ans = 1
else:
    if x3 == x4:
        if min(x1, x2) <= x3 <= max(x1, x2) and min(y3, y4) <= (y2 - y1) * (x3 - x1) / (x2 - x1) + y1 <= max(y3, y4):
            ans = 1
    elif y3 == y4:
        if min(y1, y2) <= y3 <= max(y1, y2) and min(x3, x4) <= (x2 - x1) * (y3 - y1) / (y2 - y1) + x1 <= max(x3, x4):
            ans = 1
    else:
        A = y2 - y1
        B = x2 - x1
        C = y4 - y3
        D = x4 - x3
        K = D * A - B * C
        
        if K == 0:
            if B * (y3 - y1) == A * (x3 - x1) and (min(x1, x2) <= x3 <= max(x1, x2) or min(x1, x2) <= x4 <= max(x1, x2) or min(x3, x4) <= x1 <= max(x3, x4) or min(x3, x4) <= x2 <= max(x3, x4)):
                ans = 1
        else:
            Kx = B * D * y3 - D * B * y1 + D * A * x1 - B * C * x3
            if min(x1, x2) <= Kx / K <= max(x1, x2) and min(x3, x4) <= Kx / K <= max(x3, x4):
                ans = 1

print(ans)