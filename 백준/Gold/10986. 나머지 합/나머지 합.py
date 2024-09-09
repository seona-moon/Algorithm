import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 구간 합 구하기
dp = [0] * (n + 1)
for i in range(n):
    dp[i + 1] = arr[i] + dp[i]

# 구간 합 나머지 업데이트
cnt = 0
for i in range(1, n + 1):
    dp[i] %= m
    if dp[i] == 0:
        cnt += 1  # 나머지가 0인 경우, 길이가 1일때 무조건 성립

# 나머지가 같은 조합의 수를 계산하는 문제로 변형
for i in range(m):  # m으로 나눈 나머지는 0~m-1 밖에 없음.
    num = 0  # 나머지가 같은 값의 개수
    for j in range(1, n + 1):
        if dp[j] == i:
            num += 1  # 나머지가 같은 값들을 다 더한다.
    if num >= 2:
        cnt += num * (num - 1) / 2  # nC2를 계산
print(int(cnt))
