# 실패한 풀이. 만약 길이가 1인 내부 지점을 지나게 된다면 1111이기 때문에 인식하지 못하게 됨.
# 점이 아니라 선을 기준으로 보아야 했음...ㅠㅠ
rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    dx = [1,0,-1,0,1,-1,1,-1]
    dy = [0,1,0,-1,1,1,-1,-1]
    
    # 사각형 맵 만들기
    map = [[0]*20 for _ in range(20)]
    for rec in rectangle:
        sx, sy, ex, ey = rec
        for x in range(sx,ex+1):
            for y in range(sy,ey+1):
                map[x][y]=1
    visited = [[0]*20 for _ in range(20)]
    q = deque()
    visited[characterX][characterY]=0
    q.append([characterX, characterY])
    
    # 해당 점의 8방향에 0의 값이 하나라도 있으면 가장자리
    def search(x, y):
        for i in range(8):
            mx = x + dx[i]
            my = y + dy[i]
            if map[mx][my]==0: return True
        return False
    while q:
        # 큐에서 뺀다
        x, y = q.popleft()

        # 순회
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            # 방문할 수 있는가? + 해당 점이 0과 접하는가? + 방문하지 않았는가?
            if map[mx][my]==1 and visited[mx][my]==0:
                if characterX==mx and characterY==my: continue
                if search(mx,my):
                    visited[mx][my] = visited[x][y]+1
                    q.append([mx, my])
                    if mx==itemX and my==itemY:
                        return visited[itemX][itemY]

print(solution(rectangle, 1, 3, 7, 8)) #return 10