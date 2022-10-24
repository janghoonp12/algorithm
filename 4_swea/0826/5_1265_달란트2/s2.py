T = int(input())
for t in range(1, T+1):
    N, P = map(int, input().split())
    arr = [N // P] * P
    for i in range(N % P):
        arr[i] += 1
    
    ans = 1
    for i in arr:
        ans *= i

    print(f'#{t}', ans)