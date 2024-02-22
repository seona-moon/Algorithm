n = int(input())

m = []
d = [[0]*(n+1) for _ in range(n+1)]

# 맵 초기화
for i in range(n):
    a = list(map(int,input().split()))
    m.append(a)

# dp 초기화
for i in range(1, n+1):
    for j in range(1, i+1):
        if i==j and i==1:
            d[1][1] = m[0][0] # 초기값
        d[i][j] = max(d[i-1][j],d[i-1][j-1]) + m[i-1][j-1]

print(max(d[n]))
