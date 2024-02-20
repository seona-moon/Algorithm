import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
vert = []
parent = [i for i in range(n+1)]

def union(a,b):
    aParent = find(a)
    bParent = find(b)
    if aParent == bParent: return
    if aParent < bParent:
        parent[bParent] = aParent
    else:
        parent[aParent] = bParent

def find(a):
    if parent[a] == a:
        return a
    else:
        return find(parent[a])

for _ in range(m):
    # a - b 연결 (가중치 c)
    a, b, c = map(int,input().split())
    vert.append([a,b,c])

vert.sort(key=lambda x:(x[2]))
ans = 0
for v in vert:
    a,b,cost = v
    # 두 노드의 부모가 같으면 연결하면 안된다 (사이클 점검)
    if find(a) != find(b):
        union(a,b)
        ans += cost

print(ans)

    