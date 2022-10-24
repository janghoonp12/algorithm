N = int(input())
W = input()

L = 2
for i in range(len(W) - 1):
    if i > 0 and W[i] == W[i-1]:
        continue
    
    li = [W[i]]
    c = 1
    for j in range(i + 1, len(W)):
        if W[j] not in li:
            li.append(W[j])
            if len(li) > N:
                if c > L:
                    L = c
                break
        
        c += 1
        if j == len(W) - 1 and c > L:
            L = c
            
print(L)
