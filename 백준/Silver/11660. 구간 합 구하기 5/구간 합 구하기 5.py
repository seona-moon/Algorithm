import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = []
dp = [[0]*(n+1) for _ in range(n+1)]

# 맵 받아오기
for i in range(n):
    row = list(map(int, input().split()))
    maps.append(row)

# dp 계산
for i in range(1, n+1):
    for j in range(1,n+1):
        if i==j and i==1:
            dp[1][1] = maps[0][0]
            continue
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + maps[i-1][j-1]

# 합 계산
for _ in range(m):
    x1, y1, x2, y2 = map(int,input().split())
    total = dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1]
    print(total)