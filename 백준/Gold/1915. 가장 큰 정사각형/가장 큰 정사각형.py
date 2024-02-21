import sys
input = sys.stdin.readline

n, m = map(int,input().split())

a = [[0]*(m+1)]
d = [[0]*(m+1) for _ in range(n+1)]

for _ in range(n):
    row = input().strip()
    li = [0]
    li.extend([int(i) for i in row])
    a.append(li)

size = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i][j]:
            d[i][j]=min(d[i-1][j-1],d[i-1][j],d[i][j-1])+1
            size = max(size, d[i][j])

print(size**2)