from sys import stdin
I = stdin.readline

def group(M, li, m):
    if max(li) > m:
        return False
       
    group = 0
    g_sum = 0
    p = 0
    while True:
        if g_sum + li[p] > m:
            group += 1
            g_sum = 0
            
        g_sum += li[p]
        
        if p == len(li) - 1:
            group += 1
            break
        else:
            p += 1
    
    if group > M:
        return False
    else:
        return True
    
def arr(N, M, li, ans):
    p = 0
    group = 0
    g_sum = 0
    g_count = 0
    count_li = []
    while True:
        if p == N - M + group + 1:
            count_li.append(g_count)
            count_li += [1] * (M - group - 1)
            return count_li
        
        if g_sum + li[p] > ans:
            count_li.append(g_count)
            group += 1
            g_count = 0
            g_sum = 0
        
        g_sum += li[p]
        g_count += 1
        
        if p == len(li) - 1:
            count_li.append(g_count)
            group += 1
            break
        else:
            p += 1
            
    return count_li
        

N, M = map(int, I().split())
li = list(map(int, I().split()))

s = 1
e = 30000
ans = 0
gn = []
while s <= e:
    m = (s + e) // 2
    if group(M, li, m):
        e = m - 1
        ans = m
    else:
        s = m + 1
        
print(ans)
print(*arr(N, M, li, ans))