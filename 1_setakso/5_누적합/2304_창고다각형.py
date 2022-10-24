from sys import stdin
I = stdin.readline

N = int(input())
li = []

M = 0
for _ in range(N):
    L, H = map(int, I().split())
    li.append([L, H])
    M = max(M, H)
li.sort()

new_arr_1 = [0]*1001
m_1 = 0
for i in range(len(li)):
    m_1 = max(m_1, li[i][1])
    for j in range(li[i][0], 1001):
        new_arr_1[j] = m_1

new_arr_2 = [0]*1001
m_2 = 0
for i in range(1, len(li)+1):
    m_2 = max(m_2, li[-i][1])
    for j in range(li[-i][0], 0, -1):
        new_arr_2[j] = m_2

print(sum(new_arr_1) + sum(new_arr_2) - 1000*M)
