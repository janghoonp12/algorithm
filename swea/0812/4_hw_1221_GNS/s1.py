# import sys
# sys.stdin = open('input.txt', 'r')

wnum = ['ZRO', 'ONE', 'TWO', 'THR','FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for t in range(1, T+1):
    t, n = input().split()
    n = int(n)
    arr = list(input().split())
    count = [0]*10
    for i in arr:
        for j in range(10):
            if i == wnum[j]:
                count[j] += 1
    
    print(t)
    for i in range(10):
        for _ in range(count[i]):
            print(wnum[i], end=' ')
    print()
