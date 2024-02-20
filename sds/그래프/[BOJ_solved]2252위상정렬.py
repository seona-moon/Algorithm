import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
inDegree = [0]*(n+1) # 진입 차수 (포인팅의 개수)
adj = [[] for _ in range(n+1)] # [[]]*(n+1)로 진행하면 모두 같은 리스트기 때문에 에러 발생!!
q = deque() # 큐 형식으로 작성


for _ in range(m):
    # a가 b앞에 서야 한다 (a < b)
    a, b = map(int, input().split())
    adj[a].append(b) # a를 포인팅하고있는 간선 b 추가! (리스트로 작성)
    inDegree[b] += 1

# 출력
for i in range(1,n+1):
    # 시작 정점
    if inDegree[i] == 0:
        q.append(i)
        print(i," ",end="")

# 정점을 돌면서 값 찾기
while(q):
    rootnode = q.popleft()
    for node in adj[rootnode]:
        inDegree[node] -= 1
        if inDegree[node]==0:
            q.append(node)
            print(node," ",end="")