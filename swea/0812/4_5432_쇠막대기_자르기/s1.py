# import sys
# sys.stdin = open('input.txt', 'r')
'''
r()(((()())(())()))(())
01012343432343232101210
  0    3 31  31 211  11

'''
T = int(input())
for t in range(1, T+1):
    S = input()
    x = 0
    count = 0
    for i in range(len(S)):
        if S[i] == ')':
            x -= 1
            if S[i-1] =='(':
                count += x
            else:
                count += 1
        else:
            x += 1
    print(f'#{t} {count}')
