# import sys
# sys.stdin = open('input.txt', 'r')


T = int(input())
for t in range(1, T+1):
    P, A, B = map(int, input().split())
    start_a = start_b = 1
    end_a = end_b = P
    count_a = count_b = 0
    
    while start_a <= end_a:
        count_a += 1
        mid_a = int((start_a + end_a) / 2)
        if mid_a == A:
            break
        elif mid_a < A:
            start_a = mid_a
        else:
            end_a = mid_a
    
    while start_b <= end_b:
        count_b += 1
        mid_b = int((start_b + end_b) / 2)
        if mid_b == B:
            break
        elif mid_b < B:
            start_b = mid_b
        else:
            end_b = mid_b
    
    if count_a == count_b:
        win = 0
    elif count_a < count_b:
        win = 'A'
    else:
        win = 'B'
    print(f'#{t} {win}')