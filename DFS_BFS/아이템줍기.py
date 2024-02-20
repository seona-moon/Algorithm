rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    # 사각형 맵 만들기
    map = [[0]*51 for _ in range(51)]
    for rec in rectangle:
        sx, sy, ex, ey = rec
        for x in range(sx,ex+1):
            for y in range(sy,ey+1):
                map[x][y]=1
    visited = [[0]*51 for _ in range(51)]
    q = deque()
    visited[characterX][characterY]=1
    q.append([characterX, characterY,0])
    
    # 해당 점의 상하좌우에 0의 값이 하나라도 있으면 가장자리
    def search(x, y):
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if map[mx][my]==0: return True
        return False
    
    count = 0
    while q:
        # 큐에서 뺀다
        x, y, count = q.popleft()
        # 목적지인가?
        if x==itemX and y==itemY:
            return count
        # 순회
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            # 방문할 수 있는가? + 해당 점이 0과 접하는가? + 방문하지 않았는가?
            if map[mx][my]==1 and visited[mx][my]==0:
                if search(mx,my):
                    visited[mx][my] = 1
                    q.append([mx, my, count+1])

solution(rectangle, 1, 3, 7, 8) #return 17

#  2, 4에서 문제 발생 -> 디버깅하기