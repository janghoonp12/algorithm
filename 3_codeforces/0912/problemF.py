from sys import stdin, stdout
input = stdin.readline
print = stdout.write

for t in range(int(input())):
    s = input()[:-1]
    n = len(s)
    arr = [0] * (n + 1)
    for i in range(1, n + 1):
        arr[i] = int(s[i - 1])
        
    w, m = map(int, input().split())
    prefix = [0] * (n - w + 2)
    prefix[1] = sum(arr[1 : w + 1]) % 9
    for i in range(2, n - w + 2):
        prefix[i] = (prefix[i - 1] - arr[i - 1] + arr[i + w - 1]) % 9
    
    index = [[] for i in range(9)]
    for i in range(1, n - w + 2):
        if len(index[prefix[i]]) < 2:
            index[prefix[i]].append(i)

    ans_arr = [[(0, 0) for j in range(9)] for i in range(9)]
    
    for i in range(9):
        for j in range(9):
            li = []
            for a in range(9):
                for b in range(9):
                    if index[a] and index[b] and (a * i + b) % 9 == j:
                        if a == b:
                            try:
                                li.append((index[a][0], index[b][1]))
                            except:
                                continue
                        else:
                            li.append((index[a][0], index[b][0]))
            if li:
                ans_arr[i][j] = sorted(li)[0]
    
    for q in range(m):
        l, r, k = map(int, input().split())
        num = sum(arr[l: r + 1]) % 9
        ans = ans_arr[num][k]
        if ans == (0, 0):
            print(f'-1 -1\n')
        else:
            print(f'{ans[0]} {ans[1]}\n')