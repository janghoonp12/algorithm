from sys import stdin
I = stdin.readline

N, K, B = map(int, I().split())

li = [0] * N                # 0으로 된 N짜리 리스트 생성
for i in range(B):
    li[int(I())-1] = 1      # 고장난 위치 1로 변경
li.append(0)

C = L = sum(li[:K])

for i in range(N - K + 1):
    L += li[i + K] - li[i]
    if L < C:
        C = L

print(C)
