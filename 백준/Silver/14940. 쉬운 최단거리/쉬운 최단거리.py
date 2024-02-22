from collections import deque

# 원래 갈 수 없는 땅인 위치는 0을 출력하고, 
# 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.

dx=[1, -1, 0, 0]
dy=[0, 0, -1, 1]

n, m = map(int,input().split())
maps = []
visited = [[0]*(m) for _ in range(n)]
q = deque()

x, y = 0, 0
for i in range(n):
    row = list(map(int,input().split()))
    if row.count(2):
        x = i
        y = row.index(2)
    maps.append(row)
fx, fy = x, y
q.append([x,y])
visited[x][y] = 0

# 거리 출력
while q:
    x, y = q.popleft()
    for i in range(4):
        mx = x+dx[i]
        my = y+dy[i]
        if mx>=0 and mx<n and my>=0 and my<m:
            if not visited[mx][my] and maps[mx][my]:
                if mx==fx and my==fy: continue
                visited[mx][my] = visited[x][y]+1
                q.append([mx,my])

# 갈 수 있는데, 도달할 수 없는 곳 -1 출력
for i in range(n):
    for j in range(m):
        if visited[i][j]==0 and maps[i][j]==1:
            print(-1, end=" ")
        else:
            print(visited[i][j], end=" ")
    print()