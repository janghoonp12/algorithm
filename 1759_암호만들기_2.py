from sys import stdin
input = stdin.readline

def recur(cur, password):
    if cur == C:
        if len(password) == L:
            count = 0
            for i in password:
                if i in 'aeiou':
                    count += 1
            if 0 < count < L-1:
                print(password)
        return

    recur(cur + 1, password + arr[cur])
    recur(cur + 1, password)


L, C = map(int, input().split())
arr = sorted(list(input().split()))

recur(0, '')