n = int(input())
ans = 0

for i in range (2, n//2 +1):
    ans += (n//i -1)*i
    ans %= 10**6

print(ans)


'''
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ...
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 2 0 2 0 2 0 2 0 2 0 2 0
0 0 0 0 0 3 0 0 3 0 0 3 0 0 3
0 0 0 0 0 0 0 4 0 0 0 4 0 0 0
0 0 0 0 0 0 0 0 0 5 0 0 0 0 5
0 0 0 0 0 0 0 0 0 0 0 6 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 7 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
...
1~n까지인 경우
 처음 1*n 빼고
 2, 3, 4, 5, ... , n 빼고
 ㅈ



'''
