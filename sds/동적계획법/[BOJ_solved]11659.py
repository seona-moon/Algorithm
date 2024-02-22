import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
dp = [0]*(n+1)

dp[0] = 0
dp[1] = array[0]
for i in range(2,n+1):
    dp[i] = dp[i-1]+array[i-1]

for _ in range(m):
    s, e = map(int,input().split())
    print(dp[e]-dp[s-1])