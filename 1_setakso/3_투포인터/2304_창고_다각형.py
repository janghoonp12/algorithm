'''
창고 다각형의 넓이를 각 층 별로 나눠서 계산합니다.
1층(높이 0~1)에서 창고에 해당하는 넓이는 H값(높이)이 1이상인 기둥의
(max L 값 +1) - min L 값
1층부터 넓이를 누적 하여 창고 다각형의 넓이를 계산할 수 있습니다.
'''
N = int(input())                   # 입력값 받기
li = []
for i in range(N):
    li.append(list(map(int, input().split())))

area = 0
for j in range(1001):              # j ~ j+1 높이 확인
    L = []
    for k in li:                   # 높이가 j보다 큰 기둥 모으기
        if k[1] > j:
            L.append(k[0])
    if not L:                      # L이 빈 리스트일 경우 break
        break    
    area += (max(L) + 1) - min(L)  # 모은 기둥들의 L값 min, max로 창고 넓이 누적합   
        
print(area)                        # 넓이 출력