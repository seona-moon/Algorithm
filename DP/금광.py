
n, m = map(int, input().split())
array = list(map(int, input().split()))

# 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
dp = []
index = 0
for i in range(n):
    #슬라이싱을 바탕으로 2차원 배열 생성
    dp.append(array[index:index + m])
    index += m

# 각 열마다 순회 (첫번째 열은 아무거나 선택 가능)
for i in range(1,m): #m:열
    for j in range(n): #n:행 (n,m)
        #왼쪽 위
        left_top = 0 if j - 1 < 0 else dp[j-1][i-1]
        #왼쪽 중간
        left_mid = dp[j][i-1]
        #왼쪽 밑
        left_bot = 0 if j + 1 >= n else dp[j+1][i-1]
        
        dp[j][i] += max(left_top,left_mid,left_bot)

result = 0
for i in range(n):
    result = max(result, dp[i][m-1])
print(result)