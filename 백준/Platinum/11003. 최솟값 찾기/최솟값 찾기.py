from collections import deque
import sys

input = sys.stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))
d = deque()  # 최솟값을 기록할 덱

for i in range(n):
    # 최솟값 업데이트 - (덱에 값이 있을 떄) 덱의 오른쪽에서부터 본인보다 작은 값 삭제
    while d and d[-1][1] > arr[i]:
        d.pop()
    d.append([i, arr[i]])  # 본인 값 추가
    # 슬라이딩 윈도우 크기 조사
    if d[0][0] <= i - l:  # 범위가 아닌 값 삭제
        d.popleft()
    print(d[0][1], end=" ")  # 현재 최솟값 출력
