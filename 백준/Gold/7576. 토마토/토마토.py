from collections import deque

m, n = map(int,input().split())
box = []
visited = [[0]*(m) for i in range(n)]
for _ in range(n):
    box.append(list(map(int,input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
q = deque()

# -1의 개수 세기
dummy=0
# 익은 토마토의 위치 저장
for i in range(n):
    for j in range(m):
        if box[i][j]==1: 
            q.append([i,j,0])
            visited[i][j] = 1
        if box[i][j]==-1:
            dummy+=1

# 이미 모든 토마토가 익어 있다면?
if len(q)+dummy==n*m:
    print(0)
    exit()
    
if len(q)==0:
    print(-1)
    exit()

while q:
    x, y, day = q.popleft()
    #완료 조건
    for i in range(4):
        mx = x+dx[i]
        my = y+dy[i]
        if mx>=0 and mx<n and my>=0 and my<m:
            if not visited[mx][my] and box[mx][my]==0:
                visited[mx][my] = 1
                box[mx][my] = day + 1
                q.append([mx,my,day+1])

day = 0
for i in range(n):
    for j in range(m):
        # 안익은 토마토가 존재한다면
        if not box[i][j]: 
            print(-1)
            exit()
        day = max(box[i][j], day)

print(day)