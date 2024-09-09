import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Prefix Sum 배열 생성
prefix_sum = [0] * n
prefix_sum[0] = arr[0]

# 구간 합 구하기
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

# 테스트 케이스 진행
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        print(prefix_sum[b - 1])
    else:
        print(prefix_sum[b - 1] - prefix_sum[a - 2])
