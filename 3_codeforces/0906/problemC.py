for t in range(int(input())):
    n = int(input())
    bracket = input()
    
    count = 0
    for i in range(2*n - 1):
        if bracket[i] == ')' and bracket[i+1] == '(':
            count += 1
    print(n - count)