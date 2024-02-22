from collections import deque

dx=[1, -1, 0, 0]
dy=[0, 0, -1, 1]

n, m = map(int,input().split())
map = []
visited = [[0]*(m) for _ in range(n)]
q = deque()

for _ in range(n):
    row = input()
    rows = [int(i) for i in row]
    map.append(rows)

q.append([0,0])
visited[0][0] = 1

while q:
    x, y = q.popleft()
    for i in range(4):
        mx = x+dx[i]
        my = y+dy[i]
        if mx>=0 and mx<n and my>=0 and my<m:
            if not visited[mx][my] and map[mx][my]:
                visited[mx][my] = visited[x][y]+1
                q.append([mx,my])

print(visited[n-1][m-1])