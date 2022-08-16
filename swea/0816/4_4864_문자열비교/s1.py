# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

    i = j = ans = 0
    while i+j < M:
        if str2[i+j] == str1[j]:
            j += 1
        else:
            i += 1
            j = 0
        
        if j == N:
            ans = 1
            break
    
    print(f'#{t} {ans}')