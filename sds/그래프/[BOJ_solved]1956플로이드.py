import sys
input = sys.stdin.readline
n, m = map(int, input().split())

MAX = sys.maxsize
d = [[MAX]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    d[i][i] = 0

for _ in range(m):
    s, e, w = map(int, input().split())
    d[s][e] = min(w, d[s][e])

minimum = MAX
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            d[i][j] = min(d[i][j],d[i][k]+d[k][j])


for i in range(1, n+1):
    for j in range(1, n+1):
        if i!=j:
            minimum = min(minimum, d[i][j]+d[j][i])
print(minimum if minimum!=max else -1)