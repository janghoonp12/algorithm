# import sys
# sys.stdin = open('input.txt', 'r')

def my_sum(x):
    s = 0
    for i in x:
        s += i
    return s

def my_mult(x):
    m = 1
    for i in x:
        m *= i
    return m

T = int(input())
for t in range(1, T+1):
    N = int(input()) // 10
    num = [1, 2]
    stack = [0]*(N+1)
    top = -1
    ans = 0

    while True:
        if my_sum(stack[:top+1]) < N:
            top += 1
            stack[top] = 1
        else:   # my_sum(stack[:top+1]) == 5: 1씩 더해서 넘어갈 일 없음
            ans += my_mult(stack[:top+1])
            top -= 1
            while stack[top] == 2:
                top -= 1 
            stack[top] = 2

        if top == -1:
            break
        
    print(f'#{t} {ans}')            


'''
1
11
111
1111
11111

1111
1112

111
112
1121

112
11
12
121
1211

121
122

12
1
2
21
211
2111

211
212

21
22
221

22
2
end
'''