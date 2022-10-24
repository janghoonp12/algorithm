from sys import stdin
I = stdin.readline

H, W = map(int, I().split())
arr = [0] + list(map(int, I().split())) + [0]

new_arr = arr[:]
for i in range(1, W+1):
    r = max(arr[0:i])
    l = max(arr[i+1:W+2])
    m = max(min(r, l), new_arr[i])
    new_arr[i] = m

rain = 0
for i in range(len(arr)):
    rain += new_arr[i] - arr[i]
    
print(rain)
    
    
'''
            x
      x o o . o o o x
x o o . o o . o . o . o x
. . . . . . . . . . . . . o o o x
                        . . . . .

'''