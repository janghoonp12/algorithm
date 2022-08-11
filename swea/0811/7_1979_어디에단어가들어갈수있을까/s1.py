import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                pass
            