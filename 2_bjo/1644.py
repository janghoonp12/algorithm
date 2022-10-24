from sys import stdin, stdout
I = stdin.readline
P = stdout.write

N = int(I())
li = [False, False] + [True]*(N-1)
print(li, len(li))