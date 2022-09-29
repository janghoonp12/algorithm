numb = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    check = False
    arr = []
    for i in range(N):
        I = input()
        if not check and int(I):
            secret_code = I
            check = True
        else:
            continue
        
    secret_number = [0] * 8
    i = M - 1
    while i >= 0:
        if secret_code[i] == '1':
            for j in range(7, -1, -1):
                secret_number[j] = numb[secret_code[i - 6 : i + 1]]
                i -= 7
            break
        i -= 1
    
    num = 0
    for j in range(8):
        if not j % 2:
            num += 3 * secret_number[j]
        else:
            num += secret_number[j]
    
    ans = 0
    if not num % 10:
        ans = sum(secret_number)
    
    print(f'#{t}', ans)