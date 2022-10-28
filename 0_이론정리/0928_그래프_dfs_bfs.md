# 9월 28일 그래프 dfs/bfs

- 선형자료구조
  - 데이터가 들어온 순서가 의미가 있음
    - 스택
    - 큐
    - 덱

- 비선형자료구조(오늘 주제)
  - 객체들의 관계를 나타내는 자료구조
    - 그래프
    - 트리
  - 무서워하는 것들
    - 쥐 -> 고양이 -> 사람 -> 바퀴벌레 -> 쥐
  - 단방향그래프
  - 무향그래프/양방향그래프


- 노드/정점
- 간선/엣지


- 무향 그래프

- 연결요소

- 하나의 그래프 4개의 연결요소

## dfs
- dfs depht 어쩌구 깊이우선탐색
  - 효과
    - 하나의 그래프 여러개의 연결요소
    - dfs하면 시작점이 포함된 연결요소의 노드를 모두 방문
    - 연결요소의 갯수, 크기, 한연결요소의 정보를... 할때 dfs 사용

- 인접 행렬(안씀)
    1 2 3 4 5 6 7
1   0 0 0 0 0 0 0
2   0 0 0 0 0 0 0
3   0 0 0 0 0 0 0 
4   0 0 0 0 0 0 0 
5   0 0 0 0 0 0 0 
6   0 0 0 0 0 0 0 
7   0 0 0 0 0 0 0 



- 인접 리스트
```python
'''
1   [2, 5]
2   [1, 3, 5]
3   [2]
4   [7]
5   [1, 2]
6   [5]
7   [4]

2차원 리스트 사용
v = [[], [2, 5], [1, 3, 5], [2], ...]

v[1] -> [2, 5]
v[2] -> [1, 3, 5]
...
'''
n = int(input())
m = int(input())
v = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    
    v[a].append(b)
    v[a].append(a)
```

### 바이러스 문제
- 1번 요소가 속한 연결요소의 크기 구하는 문제


- 기본 코드
```python
def dfs(cur):
    global cnt
    ## cnt = 1

    cnt += 1
    visited[cur] = True

    for nxt in v[cur]:
        if visited[nxt]:
            continue
        
        ## cnt += dfs(nxt)

        dfs(nxt)


n = int(input())
m = int(input())
v = [[] for i in range(n + 1)]
visited = [False for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    
    v[a].append(b)
    v[a].append(a)

cnt = 0
dfs(1)

print(cnt - 1)
# print(visited.count(True) - 1)
## print(dfs(1))
```


### 연결 요소의 개수
```python
def dfs(cur):
    visited[cur] = True
    for nxt in v[cur]:
        if visited[nxt]:
            continue
        
        dfs(nxt)


n, m = map(int, input().split())
v = [[] for i in range(n + 1)]
visited = [False for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    
    v[a].append(b)
    v[b].append(a)

cnt = 0
for i in range(1, n + 1):
    if visited[i]:
        continue
    
    cnt += 1
    dfs(i)

print(cnt)
```




- 플러드필
  - 지도가 있음
0 땅, 1 물
섬이 몇개?
웅덩이 몇개?

0 1 1 1 0 0 1 0 0 0
1 0 0 0 0 0 1 1 1 1
1 0 0 0 0 0 1 1 1 1
0 0 0 0 0 0 0 0 0 0 
- dfs, bfs 둘다 사용가능


### 단지번호붙이기
- 플러드필
- 섬의 갯수와 섬의 크기 오름차순 출력문제

- 그래프의 형태가 이상할 뿐, 연결요소 크기, 갯수 구하는 문제
  - 노드 번호 -> 노드 좌표

```python
def dfs(x, y):
    global cnt2

    cnt2 += 1
    visited[x][y] = True
    for i in range(4)
        nx = x + dx[i]
        ny = y + dy[i]
        
        if not (0 <= nx < n and 0 <= ny < n) or arr[nx][ny] != '1' or visited[nx][ny]:
            continue
        
        dfs(nx, ny)


N = int(input())
arr = [input() for i in range(N)]
visited = [[False for i in range(N)] for j in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0 ,-1]
answer = []

cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == '0' or visited[i][j]:
            continue
        
        cnt += 1
        cnt2 = 0
        dfs(i, j)
        answer.append(cnt2)

print(cnt)
print(*sorted(answer))
```



## bfs
- queue라는 자료구조 주로 사용
- dfs 하는거(오늘배운거) 대부분 할 수 있음
- 크기, 갯수, 플러드필 등
- dfs만 써야하는 경우도 있음
- 최단거리 구할 수 있음


from collections import deque 하면 풀리는데 queue = [] 하고 queue.pop(0) 하면 시간초과 나는 경우가 있던데 그냥 import 하면 되나요?

### 숨바꼭질
- 단방향 그래프 문제
- deque : double ended queue
- 
```python
n, m = map(int, input().split())

visited = [False for i in range(300010)]
dist = [0 for i in range(300010)] # 1. 일반적인 방법

mul = [1, 1, 2]
add = [-1, 1, 0]

que = deque()

que.append(n)
visited[n] = True
while len(que) > 0:
    cur = que[0]
    que.popleft()

    for i in range(3):
        nxt = mul[i] * cur + add[i]
        if 0 <= nxt < 300010 and not visited[nxt]:
            que.append(nxt)
            visited[nxt] = True
            dist[nxt] = dist[cur] + 1

print(dist[m])
```


```python
n, m = map(int, input().split())

visited = [False for i in range(300010)]
dist = [0 for i in range(300010)] # 1. 일반적인 방법

mul = [1, 1, 2]
add = [-1, 1, 0]

que = deque()

que.append(n)
visited[n] = True
while len(que) > 0:
    cur = que[0]
    que.popleft()

    for i in range(3):
        nxt = mul[i] * cur + add[i]
        if 0 <= nxt < 300010 and not visited[nxt]:
            que.append(nxt)
            visited[nxt] = True
            dist[nxt] = dist[cur] + 1

```
1. dist
2. queue에 같이 넣는것
3. queue에 사이즈???
