#https://cheon2308.tistory.com/entry/%EB%B0%B1%EC%A4%80-11049%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%96%89%EB%A0%AC-%EA%B3%B1%EC%85%88-%EC%88%9C%EC%84%9C

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
# 곱셈의 최소 횟수 행렬
dp = [[0]*N for _ in range(N)]

for diagonal in range(1, N):  # dp[i][i]는 자기 자신의 행렬이기 때문에 값이 0
    for i in range(0, N-diagonal):  # 대각선의 우측 한 칸씩 이동
        j = i + diagonal  # 현재 대각선에서 몇 번째 원소인지
        # 차이가 1밖에 나지 않는 칸 > 초기연산 (a[i]와 a[j] 연산횟수)
        if diagonal == 1: 
            dp[i][j] = a[i][0] * a[j][0] * a[j][1]
            continue

        dp[i][j] = float('inf')
        # 각 부분행렬의 곱셈 횟수 + 두 행렬의 곱셈 횟수
        for k in range(i, j):  # k값으로 최적분할 찾기
            # dp[i][k] + dp[k+1][j] -> 두 분할 중 어떤 것을 먼저 계산할 것인지!
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + a[i][0] * a[k][1] * a[j][1])

print(dp[0][N-1])