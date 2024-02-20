import sys
from heapq import *

input = sys.stdin.readline

N = int(input())
M = int(input())

def prim(node):
    INF = 10001
    visited = [0] * (N + 1) # 현재 MST에 포함된 노드들
    weight = [INF] * (N + 1) # 각 노드별 MST에 포함될 때의 소비한 가중치
    weight[node] = 0 # 시작 노드의 가중치는 0
    heap = [(0, node)]
    heapify(heap)
    
    while heap:
        # 현재 힙에서 최소 가중치의 노드 추출 (힙이 최소힙 로직)
        nowW, nowN = heappop(heap)
        # 방문한 적 없는 노드에 접근
        if not visited[nowN]:
            visited[nowN] = 1 # MST 포함
            # 노드와 연결된 간선을 힙에 넣어줌
            for w, adj in adjLst[nowN]:
                # MST의 방문하지 않은 인접노드이며 & 최솟값일 경우 업데이트
                if not visited[adj] and weight[adj] > w: 
                    weight[adj] = w
                    heappush(heap, (w, adj))      
    print(sum(weight[1:]))
                    
adjLst = [[] for _ in range(N + 1)]
# 간선 정보 추가 후 진행
for _ in range(M):
    i, j, w = map(int, input().split())
    # 무향그래프이기 때문에, 두 노드에 모두 간선의 정보를 주어야 한다.
    adjLst[i].append((w, j))
    adjLst[j].append((w, i))

prim(1) # 1번 노드부터 연결