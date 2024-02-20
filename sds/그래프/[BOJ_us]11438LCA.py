import sys
from collections import deque
input = sys.stdin.readline


DEPTH = 17
MAX = 1000001
N = int(input()) # 노드의 개수
adj = [[] for _ in range(N+1)]
parent = [[0]*(N+1) for _ in range(DEPTH)]
depth = [-1]*(N+1)
q = deque()

def lca(a, b):
    # depth 차이 계산
    if depth[a] < depth[b]: # a의 깊이가 더 깊도록 조정
        a, b = b, a
    
    # 차이가 있다면 depth를 동일하게 맞춤
    diff = depth[a] - depth[b]
    for k in range(0,K,-1):
        if diff >= 2^K: #차이가 2의 K승보다 크면 a 업데이트
            a = parent[k][a]
            diff = depth[a] - depth[b]
    # 차이가 같은데 a == b 이면 LCA!
    if a == b: return a
    
    # 차이가 같은데 a != b 이면 트리를 타고 위로 올라가면서 lca를 찾는다
    for k in range(0,K,-1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]
    return parent[0][a]
    
# K 구하기 (트리의 깊이)
K=0
n = N-1 # 간선의 개수
while (n>0):
    n //= 2
    K += 1

# bfs, dfs => parent[0] 계산 (K=0)
for _ in range(N-1): #간선의 개수
    a, b = map(int, input().split())
    # 간선 연결
    adj[a].append(b)
    adj[b].append(a)

# 1번 노드부터 방문
depth[1] = 0
q.append(1)

while(q):
    now = q.popleft()
    for next in adj[now]:
        if depth[next] == -1:
            depth[next] = depth[now] + 1
            parent[0][next] = now
            q.append(next)

# K => parent[K] 계산 (K=1 -> KMAX)
# 모르겠다 ...
for k in range(1,K):
    for v in range(N):
        parent[k][v] = parent[k-1][parent[k-1][v]]

# sparse table에서 lca 계산
m = int(input())
for _ in range(m):
    a, b = map(int,input().split())
    ans = lca(a,b)
    print(ans)