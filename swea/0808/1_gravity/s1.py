import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
for _ in range(N):
    n = int(input())
    arr = list(map(int, input().split()))
    m = 0
    ans = 0
    for i in range(n):
        if arr[i] > m:
            m = arr[i]
            count = 0
            for j in range(i+1, n):
                if arr[j] < arr[i]:
                    count += 1
            if count > ans:
                ans = count
    print(ans)