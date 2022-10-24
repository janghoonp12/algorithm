N = int(input())
S1 = list(input())
E = list(input())
for i in range(N):
    S1[i] = int(S1[i])
    E[i] = int(E[i])
S2 = S1[:]
for i in range(2):
    S2[i] = (S2[i] + 1) % 2
count1 = 0
count2 = 1
for i in range(1, N):
    if S1[i - 1] != E[i - 1]:
        count1 += 1
        for j in range(3):
            if i - 1 + j >=N:
                continue
            S1[i - 1 + j] = (S1[i - 1 + j] + 1) % 2
    if S2[i - 1] != E[i - 1]:
        count2 += 1
        for j in range(3):
            if i - 1 + j >=N:
                continue
            S2[i - 1 + j] = (S2[i - 1 + j] + 1) % 2

ans = -1
if S1 == E:
    ans = count1
elif S2 == E:
    ans = count2

print(ans)