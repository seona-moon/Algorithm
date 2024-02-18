def solution(numlist, n):
    sorted_arr = [[abs(num - n), num] for num in numlist]
    sorted_arr.sort(key=lambda x: (x[0], -x[1]))  # 거리에 따라 오름차순 정렬, 거리가 같다면 더 큰 숫자가 앞에 오도록 정렬
    return [num[1] for num in sorted_arr]