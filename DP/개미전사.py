n = int(input())
array = list(map(int, input().split()))

dp = [0]*100 #N의 최대값 100

#dp의 값은 해당 인덱스까지의 창고를 최적으로 털었을 경우를 의미
dp[0] = array[0] #0번째를 턴 경우
dp[1] = max(array[0], array[1]) #0번째 털기 vs 1번째 털기 비교

for i in range(2,n):
    #직전 방 털기(i번째는 못턺) vs 직전 방 말고 다음 방 털기
    #두 경우 중 더 큰 값으로 결정
    dp[i] = max(dp[i-1],dp[i-2]+array[i])

print(dp[n-1])