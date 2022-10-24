def recur(cur):
    global B, ans
    
    if B == 0:
        return
    if A == B:
        ans = cur
        return

    elif B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B //= 2
    else:
        return
    
    recur(cur + 1)
    
    
A, B = map(int, input().split())
ans = -1

recur(1)

print(ans)