A, B, C = map(int, input().split())

arr_A = [A % C] + [0] * 30
for i in range(1, 31):
    arr_A[i] = (arr_A[i - 1] * arr_A[i - 1]) % C

ans = 1

b = str(bin(B))[:1:-1]

for i in range(len(b)):
    if b[i] == '1':
        ans = (ans * arr_A[i]) % C

print(ans)