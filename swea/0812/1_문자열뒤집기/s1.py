# import sys
# sys.stdin = open('input.txt', 'r')

def my_sum(li):
    s = 0
    for i in li:
        s += i
    return s
    
T = int(input())
for t in range(1, T+1):
    w = input()
    print(f'#{t} {w[::-1]}')