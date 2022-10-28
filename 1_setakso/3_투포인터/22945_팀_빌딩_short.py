from sys import stdin
I = stdin.readline

N = int(I())
li = list(map(int, input().split()))

s = 0
e = N - 1
A = 0

while s + 1 < e:
    A = max(A, (e - s - 1) * min(li[s], li[e]))
    
    if li[s] < li[e]:
        s += 1
    else:
        e -= 1

print(A)

'''
      
0 1 2 3 4 5 6 7 8     
5 4 7 2 6 2 7 4 5
s               e
s           e
    s           e
    s       e
1. e가 왼쪽으로 이동하면 b는 무조건 줄어듬
2. s가 오른쪽으로 이동하면 b 줄어듬
3. 해당하는 값에 따라 min은 증가할 수 있음
4. s, e위치의 값중 작은 수를 이동(하지 않으면 min값 고정)
5. 현재의 경우는 e를 왼쪽으로 이동 e 1보다 큰값 나올때 까지
6. 값 확인후 큰 값 저장
7. 



복잡한 부분은 연산에 맡길것!
'''