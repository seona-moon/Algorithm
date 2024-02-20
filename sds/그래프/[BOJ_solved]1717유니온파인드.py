import sys
# 재귀함수를 활용할 것이므로 재귀함수의 깊이를 지정해줘야한다 !!!
# n이 백만이므로... 깊이를 늘려주지 않으면 재귀에러 발생.
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int,input().split())
parent = [i for i in range(n+1)]

def union(a, b):
    aParent = find(a)
    bParent = find(b)
    # 부모가 작은 쪽으로 연결
    if aParent == bParent: return
    if aParent < bParent:
        parent[bParent] = aParent
    else:
        parent[aParent] = bParent

def find(a):
    if parent[a]==a: return a
    else: 
        p = find(parent[a])
        parent[a] = p
        return parent[a]

for _ in range(m):
    method, a, b = map(int,input().split())
    if method==0:
        union(a,b)
    else:
        aParent = find(a)
        bParent = find(b)
        if aParent==bParent:
            print("YES")
        else:
            print("NO")