from collections import deque


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상,하,좌,우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


def bfs(x, y):
    # 시작 위치의 정보가 들어있는 queue 제작
    queue = deque([(x, y)])
    # queue가 비어있지 않으면 계속 반복
    while queue:
        # 큐에서 노드를 꺼내서 작업 시작.
        cx, cy = queue.popleft()

        # 주어진 범위를 벗어나는 경우에는 무시
        if cx < 0 or cx >= n or cy < 0 or cy >= m:
            continue

        # 현재 노드를 아직 방문하지 않았다면 (방문한 경우 그대로 끝남)
        if graph[cx][cy] == 0:
            # 해당 노드 방문 처리
            graph[cx][cy] = 1

            # 상,하,좌,우의 위치들을 큐에 삽입
            queue.append((cx - 1, cy))
            queue.append((cx, cy - 1))
            queue.append((cx + 1, cy))
            queue.append((cx, cy + 1))


# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        # if dfs(i, j):
        #    result += 1
        # 현재 위치에서 BFS 수행
        if graph[i][j] == 0:
            bfs(i, j)
            result += 1

print(result)  # 정답 출력
