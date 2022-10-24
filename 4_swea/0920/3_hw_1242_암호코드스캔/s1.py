# import sys
# sys.stdin = open('input.txt', 'r')

numb = {(3, 2, 1, 1):0, (2, 2, 2, 1):1, (2, 1, 2, 2):2, (1, 4, 1, 1):3, (1, 1, 3, 2):4, (1, 2, 3, 1):5, (1, 1, 1, 4):6, (1, 3, 1, 2):7, (1, 2, 1, 3):8, (3, 1, 1, 2):9}
change = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().strip() for i in range(N)]
    secret_code = []
    
    for i in range(N):
        temp = ''
        S = arr[i]
        if i and arr[i] == arr[i - 1]:
            continue
        for j in S:
            temp += change[j]
        
        temp = temp.rstrip('0')
        while temp:
            ind = 7
            j = len(temp) - 1
            secret_number = [0] * 8
            while ind >= 0:
                b = c = d = 0
                check = 0
                while True:
                    if check == 0:
                        if temp[j] == '1':
                            d += 1
                        else:
                            c += 1
                            check += 1
                    elif check == 1:
                        if temp[j] == '0':
                            c += 1
                        else:
                            b += 1
                            check += 1
                    elif check == 2:
                        if temp[j] == '1':
                            b += 1
                        else:
                            
                            break
                    j -= 1
                m = min(b, c, d)
                b //= m
                c //= m
                d //= m
                a = 7 - b - c - d
                secret_number[ind] = numb[(a, b, c, d)]
                j -= a * m
                ind -= 1
            if secret_number not in secret_code:
                secret_code.append(secret_number)
            temp = temp[:j].rstrip('0')
            
    ans = 0
    for i in secret_code:
        C = i[7]
        for j in range(7):
            if j % 2:
                C += i[j]
            else:
                C += 3 * i[j]
        if not C % 10:
            ans += sum(i)
    
    print(f'#{t}', ans)