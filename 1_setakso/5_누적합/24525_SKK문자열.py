from sys import stdin
I = stdin.readline

S = input()
arr = [0]
s = 0
for i in S:
    if i == 'S':
        s += 2
    elif i == 'K':
        s -= 1
    arr.append(s)

prefix = {}
suffix = {}
for i in range(len(arr)):
    prefix[arr[i]] = prefix.get(arr[i], i)
    suffix[arr[i]] = i

ans = -1
for i in prefix.keys():
    for  j in range(prefix[i], suffix[i]):
        if arr[j] != i:
            d = suffix[i] - prefix[i]
            if d > 0 and d > ans:
                ans = d
                
print(ans)