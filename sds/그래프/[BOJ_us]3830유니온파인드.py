import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 구현 필요 - a,b 연결 후 가중치 계산
# 1. 부모의 인덱스 (a, b) 찾기
# 2. 부모 위치?에 계산된 가중치 업데이트
def union(a, b):
    aParent = find(a)
    bParent = find(b)
    # 부모가 작은 쪽으로 연결
    if aParent == bParent: return
    if aParent < bParent:
        parent[bParent] = aParent
    else:
        parent[aParent] = bParent

# 구현 필요 - 부모 가중치 검색 필요
# 부모와 비교하여 차액을 더함
def find(a):
    if parent[a]==a: return a
    else: 
        p = find(parent[a])
        parent[a] = p
        return parent[a]

while(True):
    n, m = map(int, input().split())
    for _ in range(m):
        if n==0:
            break
        parent = [i for i in range(n+1)]
        
        order = list(map(str, input().split()))
        if order[0]=='!':
            a, b, w = int(order[1]), int(order[2]), int(order[3])
            
        elif order[0]=='?':
            a, b = int(order[1]), int(order[2])
            