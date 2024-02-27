import sys
sys.setrecursionlimit(10**6)

n, m = map(int,input().split())
parent = [i for i in range(n+1)]

def union(a,b):
    parentA = find(a)
    parentB = find(b)
    # 부모가 같으면 넘어감
    if parentA==parentB: return
    # 부모가 다르면 작은쪽의 부모 바꾸기
    if parentA < parentB:
        parent[parentB] = parentA
    else: 
        parent[parentA] = parentB

def find(a):
    if a==parent[a]: return a
    # 부모가 따로 존재하면, 그 부모의 부모를 찾아 조상 노드를 등록함 (parent에는 최고조상만 등록)
    parent[a] = find(parent[a])
    return parent[a]

for _ in range(m):
    method, a, b = map(int,input().split())
    # 0: 유니온, 1: 파인드
    if method==1:
        parentA = find(a)
        parentB = find(b)
        if parentA==parentB:
            print("YES")
        else: print("NO")
    elif method==0:
        union(a,b)