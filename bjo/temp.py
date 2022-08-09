from sys import stdin
I = stdin.readline

'''

10  20  3
(10-1)%3+1 = 1
(20-10)//3 = 3

->  1   10-3    3  =>   1   7   3
->  1   10+9    3  =>   1   19  3

10  13  16  19
1   4   7


'''



dic = {}

N = int(I())
for _ in range(N):
    A, C, B = map(int, I().split())
    r = (A - 1) % B + 1
    q = (C - A) // B
    n1 = (r, A - B, B)
    n2 = (r, A + q * B, B)
    for i in (n1, n2):
        if i[1] <= 0:
            continue
        elif i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
li = []
for k, v in dic.items():
    if v % 2:
        li.append(k)
li.sort(key=lambda x:(x[2],x[1]), reverse=True)
print(li)




'''

3 100 3
2 100 3
1 100 3
1 100 1
2 50 3
3 50 3
1 50 3
1 50 1

'''