# 재귀함수로 정의한 이진탐색
def binary_search(array, target, start, end):
    array.sort()  # 정렬되지 않았다면 정렬 필요
    if start > end:
        return None  # 값을 찾지 못하고 끝남
    mid = (start + end) // 2
    if target < array[mid]:
        return binary_search(array, target, start, mid - 1)
    elif target > array[mid]:
        return binary_search(array, target, mid + 1, end)
    else:  # mid가 target과 같다면?
        return mid


# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
# 이진 탐색 수행 결과 출력
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
