from collections import deque
# 가로 n, 세로 m (NxM)
n, m = map(int,input().split())
maps = []
visited = [[0]*(n) for _ in range(m)]
for _ in range(m):
    row = input()
    maps.append([i for i in row])

dx = [0,0,1,-1]
dy = [1,-1,0,0]

#병사의 합 구하기
def bfs(i,j,flag):
    q = deque()
    q.append([i,j])
    visited[i][j] = 1
    cnt = 1
    while True:
        x, y = q.popleft()
        for i in range(4):
            mx=x+dx[i]
            my=y+dy[i]
            if mx>=0 and mx<m and my>=0 and my<n:
                if flag:
                    if not visited[mx][my] and maps[mx][my]=='W':
                        cnt +=1
                        visited[mx][my] = cnt
                        q.append([mx,my])
                else: 
                    if not visited[mx][my] and maps[mx][my]=='B':
                        cnt +=1
                        visited[mx][my] = cnt
                        q.append([mx,my])
        if not q:
            return cnt
    
#내 병사의 합 구하기
myArmy = 0
for i in range(m):
    for j in range(n):
        if maps[i][j]=='W' and visited[i][j]==0:
            myArmy += bfs(i,j,1)**2

#적 병사의 합 구하기
enemyArmy = 0
for i in range(m):
    for j in range(n):
        if maps[i][j]=='B' and visited[i][j]==0:
            enemyArmy += bfs(i,j,0)**2
print(myArmy,enemyArmy)