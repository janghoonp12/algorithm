from sys import stdin
I = stdin.readline

H, W = map(int, I().split())
arr = list(map(int, I().split()))

S = sum(arr)
M = max(arr)
T = M * W
prefix = 0
suffix = 0
m_p = arr[0]
m_s = arr[W-1]
for i in range(W):
    if arr[i] > m_p:
        m_p = arr[i]
    if arr[W-1-i] > m_s:
        m_s = arr[W-1-i]        
    prefix += m_p
    suffix += m_s
rain = prefix + suffix - T - S

print(rain)
        
    
    
'''
            x
      x o o . o o o x
x o o . o o . o . o . o x
. . . . . . . . . . . . . o o o x
                        . . . . .

'''