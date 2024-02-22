n, m = map(int,input().split())

a = [[0]*(m+1)]
d = [[0]*(m+1) for _ in range(n+1)]

for _ in range(n):
    row = input()
    li = [0]
    li.extend([int(i) for i in row])
    a.append(li)

for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i][j]==0: continue
        if d[i-1][j]==0 or d[i][j-1]==0 or d[i-1][j-1]==0:
            d[i][j]=1
        else:
            d[i][j]=d[i-1][j-1]+1

ans = 0
for i in range(1,n+1):
    ans = max(ans,max(d[i]))

print(ans)