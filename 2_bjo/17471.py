def check(li):
    if not li:
        return False
    
    visited = [False] * (N + 1)
    queue = [li[0]]
    visited[li[0]] = True
    temp = [li[0]]
    while queue:
        q = queue.pop(0)
        for i in connection[q][1:]:
            if not visited[i] and i in li:
                queue.append(i)
                visited[i] = True
                temp.append(i)
    
    if set(temp) == set(li):
        return True
    else:
        return False


def is_connected():
    part2 = []
    for i in range(1, N + 1):
        if i not in part1:
            part2.append(i)
    if check(part1) and check(part2):
        return True
    else:
        return False
            

def recur(cur, p):
    global ans, t
    
    if cur == N + 1:
        if is_connected():
            ans = min(ans, abs(P - 2 * p))
            t = True
        return
    
    part1.append(cur)
    recur(cur + 1, p + population[cur])
    part1.pop()
    recur(cur + 1, p)


N = int(input())
population = [0] + list(map(int, input().split()))
connection = [0] + [list(map(int, input().split())) for i in range(N)]

ans = P = sum(population)
t = False
part1 = []

recur(1, 0)

if t:
    print(ans)
else:
    print(-1)