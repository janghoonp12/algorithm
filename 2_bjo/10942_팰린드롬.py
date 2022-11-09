from sys import stdin, stdout
input = stdin.readline
print = stdout.write

def palindrome(s, e):
    global temp
    
    if s > e:
        print(f'1\n')
        temp = 1
        return
    
    if dp[s][e]:
        print(f'{pal[s][e]}\n')
        temp = pal[s][e]
        return
    
    if arr[s] != arr[e]:
        dp[s][e] = True
        print(f'{pal[s][e]}\n')
        return
    
    palindrome(s + 1, e - 1)
    dp[s][e] = True
    if temp:
        pal[s][e] = 1


N = int(input())
arr = list(map(int, input().split()))
dp = [[False for i in range(N)] for j in range(N)]
pal = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    dp[i][i] = True
    pal[i][i] = 1

M = int(input())
for i in range(M):
    temp = 0
    S, E = map(int, input().split())
    S -= 1
    E -= 1
    palindrome(S, E)