array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):  # 0번째 인덱스는 정렬되어있다고 가정.
    for j in range(i, 0, -1):  # i에서부터 왼쪽으로 이동하며 정렬
        if array[j - 1] > array[j]:  # 만약 왼쪽 값이 더 크면 swap
            array[j - 1], array[j] = array[j], array[j - 1]
        else:  # 오른쪽 값이 더 크면 정렬 완료
            break
print(array)
