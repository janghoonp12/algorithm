import sys
sys.stdin = open('input.txt', 'r')

def li_max(li):
    m = li[0]
    for i in li:
        if i > m:
            m = i
    return m
    
for i in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for j in range(2, n-2):
        li = arr[j - 2 : j] + arr[j + 1 : j + 3] # 이부분이 지저분 하네요..
        d = arr[j] - li_max(li)
        if d > 0:
            ans += d 
    print(f'#{i} {ans}')