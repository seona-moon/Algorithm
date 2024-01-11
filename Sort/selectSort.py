array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i
    for j in range(i + 1, len(array)):  # 정렬된 값까지 조회하면 당연히 최소값이...
        if array[j] <= array[min_idx]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]
print(array)
