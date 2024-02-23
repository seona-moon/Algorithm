from collections import deque

n, l, r = map(int,input().split())
maps = []
visited = [[0]*(n) for _ in range(n)]
country = []
q = deque()

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(n):
    maps.append(list(map(int,input().split())))

# (0,0)부터 시작해서 열리는 국경 찾기
q.append([0,0])
visited[0][0] = 1
while q:
    x, y = q.popleft()
    for i in range(4):
        mx = x+dx[i]
        my = y+dy[i]
        if mx>=0 and mx<n and my>=0 and my<n and not visited[mx][my]:
            diff = abs(maps[x][y]-maps[mx][my])
            if diff>=l and diff <=r:
                country.append([mx,my])
            visited[mx][my] = 1
            q.append([mx,my])

print(country)