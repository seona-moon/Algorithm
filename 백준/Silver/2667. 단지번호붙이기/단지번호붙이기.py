from collections import deque

dx=[1, -1, 0, 0]
dy=[0, 0, -1, 1]

n= int(input())
map = []
visited = [[0]*(n) for _ in range(n)]
q = deque()

for _ in range(n):
    row = input()
    rows = [int(i) for i in row]
    map.append(rows)

def bfs(i,j):
    # 이미 방문한 단지라면 나오기
    if visited[i][j]: return 0
    
    q.append([i,j])
    cnt = 1
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if mx>=0 and mx<n and my>=0 and my<n:
                if map[mx][my] and not visited[mx][my]:
                    cnt+=1
                    visited[mx][my]=1
                    q.append([mx,my])
    return cnt

result = []

for i in range(n):
    for j in range(n):
        if map[i][j]:
            cnt = bfs(i,j)
            if cnt:
                result.append(cnt)

print(len(result))
result.sort()
for c in result: print(c)