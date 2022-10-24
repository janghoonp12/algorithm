from sys import stdin, stdout
I = stdin.readline
P = stdout.write

N = int(I())
li = list(map(int, input().split()))

def ab(x, y):
    return (y - x - 1) * min(li[x], li[y])

s = 0
e = N - 1
A = ab(s, e)


while s < e:
    u = li[s]
    v = li[e]
    if u < v:
        while s < e:
            s += 1
            if li[s] > u:
                break
            
    elif u > v:
        while s < e:
            e -= 1
            if li[e] > v:
                break   
            
    else:
        temp_s = s
        temp_e = e
        while temp_s < e:
            temp_s += 1
            if li[temp_s] > u:
                break
        while s < temp_e:
            temp_e -= 1
            if li[temp_e] > v:
                break
        if ab(temp_s, e) <= ab(s, temp_e):
            e = temp_e
        else:
            s = temp_s
        
    if ab(s, e) > A:
        A = ab(s, e)

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

'''