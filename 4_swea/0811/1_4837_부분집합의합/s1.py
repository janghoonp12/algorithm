# import sys
# sys.stdin = open('input.txt', 'r')

def my_sum(li):
    s = 0
    for i in li:
        s += i
    return s
    
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [i for i in range(1, 13)]
    count = 0
    li = [0 for _ in range(12)]
    for i in range(1<<12):
        S = 0
        temp = i
        for j in range(12):
            if temp == 1:    
                li[j] = temp
                j += 1
                while j < 12:
                    li[j] = 0
                    j += 1
                break
            else:
                li[j] = temp % 2
                temp = temp // 2
        for j in range(12):
            S += arr[j] * li[j]        
        
        if my_sum(li) == N and S == K:
            count += 1
    print(f'#{t} {count}')