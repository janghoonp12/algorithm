def dfs(cur):
    global front, middle, back
    
    if cur == ord('.'):
        return
    
    front += chr(cur)
    dfs(v[cur][0])
    middle += chr(cur)
    dfs(v[cur][1])
    back += chr(cur)


N = int(input())
v = [[] for i in range(ord('Z') + 1)]

for i in range(1, N + 1):
    a, b, c = input().split()
    
    v[ord(a)].append(ord(b))
    v[ord(a)].append(ord(c))

front = ''
middle = ''
back = ''

dfs(ord('A'))

print(front)
print(middle)
print(back)