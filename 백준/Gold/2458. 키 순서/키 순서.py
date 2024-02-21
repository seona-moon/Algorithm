import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)] #원래 순서
reverse_graph = [[] for _ in range(n+1)] #반대 순서

for _ in range(m) :
    a,b = map(int,input().split())    
    # 두 방향 다 계산 필요
    graph[a].append(b)
    reverse_graph[b].append(a)

def bfs(start,graph) :
    visited = [0] * (n+1)
    q = deque([])
    q.append(start)

    visited[start] = 1
    while q:
        now = q.popleft()

        for g in graph[now] :
            if not visited[g] :
                visited[g] = 1
                q.append(g)

    return sum(visited)

res = 0

for i in range(1,n+1) :
    # 특정 지점을 기준으로, 본인보다 키가 큰 쪽, 작은 쪽을 두번 돌려서 계산한다.
    # 그렇게 본인 기준 큰 값 + 작은 값을 더한게 n-1이라면 순서가 정해졌다는 뜻!!
    cnt = bfs(i,graph) + bfs(i,reverse_graph) - 1
    if cnt == n :
        res += 1

print(res)