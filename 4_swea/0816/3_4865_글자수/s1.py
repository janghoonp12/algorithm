# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    str1 = set(input())        
    str2 = input()
    count = {}
    
    for i in str2:
        if i in str1:
            count[i] = count.get(i, 0) + 1
    
    m = 0
    for i in count.values():
        if i > m:
            m = i
    
    print(f'#{t} {m}')