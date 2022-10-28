'''
입력값
N                               1 ~ 50만
A = {a0 a1 a2 a3 ... aN-1}      -1,000만 ~ 1,000만, 중복 없음
M                               1 ~ 50만
B = {b0 b1 b2 b3 ... bM-1}      -1,000만 ~ 1,000만

각 bi에 대해 A에 존재하는지 여부를 출력

1. 완전 탐색의 경우 50만 * 50만 -> 2,500억

2. 이진탐색 사용
    - A 정렬
    - s = 0, e = N - 1
    - 아래과정 반복
        - m = (s + e) // 2
        - A[m]과 bi 비교
        - 같으면 1 출력하고 탈출
        - A[m]이 작으면 s = m + 1
        - A[m]이 크면 e = m - 1
    - 언제까지? 
        - while s <= e: 반복
        - s = e 일 때도 확인해야함 
        - if s > e:
              0 출력하고 탈출
              
3. 오프라인 쿼리
    - B를 [[b0,0], [b1, 1], [b2, 2], ... , [bM-1, M-1]]으로 변환
    - A랑 B 둘다 정렬 후 투 포인터로 bi 존재 여부 확인
    - s1 = 0, s2 = 0
    - 아래과정 반복
        - A[s1]과 B[s2][0] 비교
        - 같으면 [B[s2][1], 1] 저장, s1, s2 += 1
        - A[s1]이 작으면 s1 += 1
        - A[s1]이 크면 s2 += 1
    - 언제까지?
        - s1 = N or s2 = M 이면 탈출
'''
# 3번 오프라인 쿼리 + 투 포인터 풀이

from sys import stdin
I = stdin.readline

N = int(I())
A = sorted(list(map(int, I().split())))
M = int(I())
B = list(map(int, I().split()))

B = list(enumerate(B))
B.sort(key=lambda x:x[1])
s = 0
li = [0] * (M)

for i in B:
    n = i[1]
    m = i[0]
    
    while s < N:
        if A[s] == n:
            li[m] = 1
            s += 1
            break
        elif A[s] > n:
            break
        else:
            s += 1
        
print(*li)