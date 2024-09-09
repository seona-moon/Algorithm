import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 구간 합 구하기
dp = [0] * n
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = arr[i] + dp[i - 1]

# 구간 합 나머지 업데이트 (동시에 나머지 배열 초기화도 같이)
cnt = 0
rem = [0] * m  # m으로 나눈 나머지는 0~m-1 밖에 없음.

for i in range(n):
    dp[i] %= m
    if dp[i] == 0:
        cnt += 1  # 나머지가 0인 경우, 길이가 1일때 무조건 성립
    rem[dp[i]] += 1  # 해당 나머지를 가진 값 +1

# 나머지가 같은 조합의 수를 계산하는 문제로 변형
for i in range(m):
    if rem[i] >= 2:
        cnt += rem[i] * (rem[i] - 1) / 2  # nC2를 계산
print(int(cnt))
