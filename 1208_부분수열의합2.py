def p_recur(cur, s):
    if cur == n:
        p_dic[s] = p_dic.get(s, 0) + 1
        return
    
    p_recur(cur + 1, s + p_arr[cur])
    p_recur(cur + 1, s)


def s_recur(cur, s):
    global ans
    
    if cur == N - n:
        ans += p_dic.get(S - s, 0)
        return
    
    s_recur(cur + 1, s + s_arr[cur])
    s_recur(cur + 1, s)


N, S = map(int, input().split())
arr = sorted(list(map(int, input().split())))
n = N // 2
p_arr = arr[:n]
s_arr = arr[n:]

p_dic = {}
p_recur(0, 0)
ans = 0
s_recur(0, 0)
if S == 0:
    ans -= 1

print(ans)