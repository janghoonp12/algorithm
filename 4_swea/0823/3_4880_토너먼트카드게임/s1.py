# import sys
# sys.stdin = open('input.txt', 'r')

def cardgame(arr):
    if len(arr) == 1:
        return 1, 1, arr[0]

    elif len(arr) == 2:
        if (3 + arr[1] - arr[0]) % 3 == 1:
            return 2, 2, arr[1]
        else:
            return 2, 1, arr[0]
            
    else:
        l1, i1, v1 = cardgame(arr[:(len(arr)+1)//2])
        l2, i2, v2 = cardgame(arr[(len(arr)+1)//2:])
        l = l1 + l2
        if (3 + v2 - v1) % 3 == 1:
            i = l1 + i2
            v = v2
        else:
            i = i1
            v = v1
        return l, i, v

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    l, i, v = cardgame(arr)
    ans = i

    print(f'#{t} {ans}')