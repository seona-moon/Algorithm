N, M = map(int, input().split()) #N개수, M목표
array = list(map(int, input().split()))

start, end = 0, max(array)
result = 0

while(start<=end) : #떡의 길이를 기준으로 정렬
    mid = (start+end)//2
    total = sum([max(int(k)-mid,0) for k in array])
    if total >= M :  #자른 길이가 목표를 충족 (길이를 더 늘려야함)
        result = mid #결과에 임시저장
        start = mid+1 
    elif total < M : #자른 길이가 부족 (길이를 더 줄여야 함)
        end = mid-1

print(result)