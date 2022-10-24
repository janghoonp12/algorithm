# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    A, B = input().split()  # 문자열 받기
    i = j = count = 0       # i,j,count 초기화
    while i + j < len(A):   # i+j가 A 문자열범위 넘어가면 탈출
        if A[i+j] != B[j]:  # 해당 위치에서 문자가 다르면
            i += 1          # 문자비교 위치 한칸 이동
            j = 0           # j 초기화
        else:
            j += 1          # 문자가 같으면 j 오른쪽으로 한칸 이동

        if j == len(B):     # B를 다 확인하면
            count += 1      # count 1 증가
            i += j          # i 위치 이동
            j = 0           # j 초기화
    
    print(f'#{t} {len(A) - count * (len(B)-1)}')
