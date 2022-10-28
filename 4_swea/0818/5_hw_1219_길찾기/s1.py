# import sys
# sys.stdin = open('input.txt', 'r')

while True:
    try:
        t, N = map(int, input().split())
        arr = list(map(int, input().split()))

        path = [[] for _ in range(100)]
        for i in range(len(arr)//2):
            path[arr[2*i]].append(arr[2*i+1])

        stack = [-1]*(101)
        top = -1
        visited = [False]*(100)
        visited[0] = True
        top += 1
        stack[top] = 0
        ans = 0

        while ans == 0 and top > -1:
            for i in path[stack[top]]:
                if i == 99:
                    ans = 1
                    break
                elif visited[i] == False:
                    top += 1
                    stack[top] = i
                    visited[i] = True
                    break
            else:
                top -= 1

        print(f'#{t} {ans}')

    except:
        break