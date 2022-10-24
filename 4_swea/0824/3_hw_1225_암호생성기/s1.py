# import sys
# sys.stdin = open('input.txt', 'r')

while True:
    try:
        t = int(input())
        queue = list(map(int, input().split()))
        n = 0
        while True:
            n += 1
            v = queue.pop(0)
            v -= (n-1)%5+1
            if v <= 0:
                queue.append(0)
                break
            else:
                queue.append(v)
        print(f'#{t}', *queue)
    except:
        break