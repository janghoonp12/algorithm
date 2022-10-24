from sys import stdin
I = stdin.readline

N = int(I())
arr = [-10**9] + list(map(int, I().split())) + [10**9]

prefix = [0]*(N+1)
count = 0
for i in range(N+1):
    prefix[i] = arr[i+1] - arr[i]
    if prefix[i] < 0:
        count += 1
        index = i
        
if count == 0:
    print(N)
elif count > 1:
    print(0)
else:
    ans = 0
    if arr[index+1] >= arr[index-1]:
        ans += 1
    if arr[index] <= arr[index+2]:
        ans += 1
    print(ans)