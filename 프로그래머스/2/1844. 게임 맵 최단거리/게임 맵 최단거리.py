from collections import deque

def solution(maps):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)]
    q = deque()
    count = 0
    
    q.append((0,0)) # 캐릭터의 위치
    visited[0][0]=1
    while(q):
        # 1. 큐에서 꺼내옴 (큐 = 내가 다음으로 방문할 곳들을 저장)
        x, y = q.popleft()
        # 2. 목적지인가? (문제에 따라 생략 가능)
        if x==n-1 and y==m-1:
            return maps[x][y]
        # 3. 연결된 곳을 순회 (현재 위치로부터 상하좌우 순회)
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            # 4. if 갈 수 있는가? (맵을 벗어나지 않고, 방문하지 않은 길(1) 이어야 함)
            if mx>=0 and mx<n and my>=0 and my<m:
                if maps[mx][my]==1 and visited[mx][my]==0:
                    # 6. 큐에 넣음
                    q.append((mx,my))
                    maps[mx][my]+=maps[x][y]
                    visited[mx][my]=1
    return -1