import sys
from collections import deque
input = sys.stdin.readline

n, m= map(int, input().split())
adj = [[] for _ in range(n+1)]
result = [0]

for _ in range(m):
    a, b = map(int,input().split())
    # A가 B를 신뢰한다
    adj[b].append(a)

# 각 노드별로 bfs 진행 -> 최대 길이 구하는 것이라서 한번에 하는게 나음!
def bfs(node):
    visited = [False] * (n + 1)
    q = deque()
    q.append(node)
    visited[node] = True
    cnt = 1
    while q:
        node = q.popleft()
        for next in adj[node]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                cnt += 1
    return cnt

for i in range(1,n+1):
    result.append(bfs(i))

m = max(result)
for i in range(1,n+1):
    if result[i]==m:
        print(i,end=' ')