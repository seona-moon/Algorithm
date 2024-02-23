#https://cheon2308.tistory.com/entry/%EB%B0%B1%EC%A4%80-11049%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%96%89%EB%A0%AC-%EA%B3%B1%EC%85%88-%EC%88%9C%EC%84%9C

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
# 곱셈의 최소 횟수 행렬
d = [[0]*N for _ in range(N)]

# 대각 행렬
# l이 4이고, 2~6을 탐색할 때 (2,3:6),(2:3,4:6),(2:4,5:6) 중 가장 작은것을 (2:6)으로 선택

for di in range(1, N):  # dp[i][i]는 자기 자신의 행렬이기 때문에 값이 0
    for i in range(0, N-di):  # 대각선의 우측 한 칸씩 이동
        j = i + di  # 현재 대각선에서 몇 번째 원소인지
        if di==1: #첫번째 사선 : 초기값
            d[i][j] = a[i][0]*a[i][1]*a[j][1]
        else:
            d[i][j] = float('inf')
            for k in range(i,j): # i~j의 중단점 : i~k / k+1~j
                d[i][j] = min(d[i][j], d[i][k]+ d[k+1][j] + a[i][0]*a[k][1]*a[j][1])
print(d[0][N-1])
