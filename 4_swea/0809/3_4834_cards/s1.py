# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    card_list = [0] * 10
    for j in range(N):
        card_list[arr[j]] += 1
    m = 0
    for j in range(10):
        if card_list[j] >= m:
            c = j
            m = card_list[j]
    print(f'#{i} {c} {m}')
