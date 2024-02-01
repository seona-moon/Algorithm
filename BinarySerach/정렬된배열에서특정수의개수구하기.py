from bisect import bisect_left, bisect_right

def count_by_range(array, left, right): #M의 왼쪽, 오른쪽 인덱스
    right_idx = bisect_right(array,right)
    left_idx = bisect_left(array,left)
    return right_idx-left_idx

N, M = map(int, input().split()) #N개의 원소 M목표
array = list(map(int, input().split()))

count = count_by_range(array,M,M)
if count==0:
    print(-1)
else:
    print(count)