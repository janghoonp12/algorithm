from sys import stdin
I = stdin.readline

N, K, B = map(int, I().split())

li = [0] * N                # 0으로 된 N짜리 리스트 생성
for i in range(B):
    li[int(I())-1] = 1      # 고장난 위치 1로 변경
li.append(0)

L = sum(li[:K])
s = 0
e = K-1
C = L

while e < N:
    if li[s]:
        L -= 1
    if li[e + 1]:
        L += 1
    s += 1
    e += 1
    if L < C:
        C = L

print(C)
            
            
            

'''
1   2   3   4   5   6   7   8   9   10
1   1           1               1   1       1   1           1       1   1       1   1   1       1           1   1   1   1   1   1       1   1
s       s           e       e

왼쪽기준                오른쪽기준                
1 -> 1 L 1개 줄어듬     1 -> 1 L 1개 늘어남     
0 -> 1 L 변화 없음      0 -> 1 L 1개 늘어남      
1 -> 0 L 1개 줄어듬     1 -> 0 L 변화 없음     
0 -> 0 L 변화 없음      0 -> 0 L 변화 없음      

1 1 0 0 1 0 0 0 1 1
s       e = s+k-1

0 0 1 1 0 1 1 1 0 0

'''