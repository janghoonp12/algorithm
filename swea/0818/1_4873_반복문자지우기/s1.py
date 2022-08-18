# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    w = list(input())
    while True:
        temp = w[:]
        stack = [0]*len(temp)
        top = -1

        for i in w:
            if stack[top] == i:
                top -= 1
            else:
                top += 1
                stack[top] = i

        w = stack[:top+1]
        if len(temp) == len(w):
            break
    
    print(f'#{t} {len(w)}')