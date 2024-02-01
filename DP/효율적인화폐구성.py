# 정수 N,M을 입력받기
N, M = map(int, input().split())
# N개의 화폐 단위 정보를 입력받기
array = []
for i in range(N):
	array.append(int(input()))

#INF로 초기화
dp = [10001]*(M+1)

#i는 확인하고자 하는 금액
dp[0] = 0
for i in range(N):
    #K는 각 화폐단위
    for k in range(array[i],M+1):
        if dp[k-array[i]]!=10001: #dp[0]=0이므로 해당 단위는 반드시 계산가능.
            dp[k]=min(dp[k],dp[k-array[i]]+1)

# 계산된 결과 출력
if dp[M] == 10001:  # 최종적으로 M원을 만드는 방법이 없는 경우
	print(-1)
else:
	print(dp[M])
        
        
        