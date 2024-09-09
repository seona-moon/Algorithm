import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
dp = [[0] * (n + 1) for _ in range(n + 1)]  # (n+1)*(n+1) 표 초기화

# 표 입력
for i in range(n):
    arr.append(list(map(int, input().split())))

# dp 초기화 (구간합 계산)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = arr[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
        # 위, 옆의 합 가져와서 구간합 계산

# 테스트 케이스 실행
for t in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(result)
