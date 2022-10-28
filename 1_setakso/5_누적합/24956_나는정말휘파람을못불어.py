N = int(input())
S = list(input())

count_E = 0
suffix_E = [0]*(N+1)
for i in range(1, N+1):
    if S[-i] == 'E':
        count_E += 1
    suffix_E[-i] = count_E

ans = 0
count_W = 0
for i in range(N):
    if S[i] == 'W':
        count_W += 1
    if S[i] == 'H':
        if suffix_E[i+1] < 2:
            continue
        else:
            ans += (count_W * ((1<<suffix_E[i+1]) - 1 - suffix_E[i+1]))%1000000007
            ans %= 1000000007
            
print(ans)
