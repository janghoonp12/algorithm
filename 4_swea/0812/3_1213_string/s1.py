# import sys
# sys.stdin = open('input.txt', 'r')

for _ in range(10):
    t = int(input())
    W = input()
    S = input()

    w = s = count = 0
    while s < len(S):
        if W[w] != S[s]:
            s -= w
            w = -1
        w += 1
        s += 1
        if w == len(W):
            count += 1
            s -= w-1
            w = 0

    print(f'#{t} {count}')