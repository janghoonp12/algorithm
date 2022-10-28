for t in range(int(input())):
    s = input()
    a = ''
    b = ''
    order = 0
    while s:
        order += 1
        if order % 2:
            print(s)
            if len(s) == 1:
                a +=s[0]
                break
            if ord(s[0]) < ord(s[-1]):
                a += s[0]
                s = s[1:]
            elif ord(s[0]) > ord(s[-1]):
                a += s[-1]
                s = s[:-1]
            elif ord(s[1]) < ord(s[-2]):
                a += s[0]
                s = s[1:]
            else:
                a += s[-1]
                s = s[:-1]
        else:
            if ord(s[0]) < ord(s[-1]):
                b += s[0]
                s = s[1:]
            elif ord(s[0]) > ord(s[-1]):
                b += s[-1]
                s = s[:-1]
            elif ord(s[1]) < ord(s[-2]):
                b += s[0]
                s = s[1:]
            else:
                b += s[-1]
                s = s[:-1]
    
    if a == b:
        print('Draw')
    else:
        arr = [a, b]
        if arr == sorted(arr):
            print('Alice')
        else:
            print('Bob')
    