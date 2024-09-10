import sys

input = sys.stdin.readline

n = int(input())  # 15,000 (재료의 개수)
m = int(input())  # 10,000,000 (갑옷 충족 번호)
arr = list(map(int, input().split()))  # 재료의 고유한 번호
arr.sort()  # 오름차순 정렬

start = 0  # 시작 인덱스
end = n - 1  # 끝 인덱스
cnt = 0

# 시작 인덱스와 끝 인덱스의 합을 비교하며 값을 줄여나가기
while start != end:
    sum = arr[start] + arr[end]
    if sum == m:  # 현재 합이 같으면 -> 아무쪽이나 옮기기
        cnt += 1
        end -= 1
    elif sum > m:  # 현재 합이 크면 -> 큰 값 - 1
        end -= 1
    else:  # 현재 합이 작으면 -> 작은 값 +1
        start += 1

print(cnt)