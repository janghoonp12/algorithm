n = int(input())
ans = []
su = []
l = [list(map(int, input().split())) for i in range(n)]

for h in range(n):
    ans=[]
    m = l.copy()
    del m[h]
    for j in range(1000):
        key = 0
        for k in range(n-1):
            if j>=m[k][0]:
                if j<m[k][1]:
                    ans.append(1)
                    key = 1
                    break
        if key == 0:
            ans.append(0)
    su.append(sum(ans))
print(max(su))
