def prime(n):
    i = 2
    while True:
        if i * i > n:
            return True
        elif n % i == 0:
            return False
        i += 1


def recur(cur, num):
    if not prime(num):
        return
    
    elif cur == N:
        print(num)
        return
    
    recur(cur + 1, num*10 + 1)
    recur(cur + 1, num*10 + 3)
    recur(cur + 1, num*10 + 5)
    recur(cur + 1, num*10 + 7)
    recur(cur + 1, num*10 + 9)


N = int(input())

recur(1, 2)
recur(1, 3)
recur(1, 5)
recur(1, 7)