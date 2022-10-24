from sys import stdin
input = stdin.readline

def d_log(num):
    i = 1
    while num >= 10 ** i:
        i += 1
    return(i)
    

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    count = 0
    
    dic_a = {}
    for i in a:
        dic_a[i] = dic_a.get(i, 0) + 1
    dic_b = {}
    for i in b:
        if dic_a.get(i, 0) > 0:
            dic_a[i] -= 1
            if dic_a[i] == 0:
                del dic_a[i]
        else:
            dic_b[i] = dic_b.get(i, 0) + 1
    
    for d in (dic_a, dic_b):
        key = list(d.keys())
        for i in key:
            if i >= 10 and d[i]:
                count += d[i]
                j = d_log(i)
                d[j] = d.get(j, 0) + d[i]
                # del d[i]          
    
    for i in range(2, 10):
        A = dic_a.get(i, 0)
        B = dic_b.get(i, 0)
        
        if A and B:
            count += abs(A - B)
        elif A:
            count += A
        elif B:
            count += B
    
    print(count)
    
            
            
