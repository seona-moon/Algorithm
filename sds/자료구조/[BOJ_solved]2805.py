import sys

n, m = map(int, sys.stdin.readline().split())
wood = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(wood)
result = 0

# 이진탐색의 끝
while(start<=end):
    mid = (start+end)//2
    add = sum([i - mid if i>=mid else 0 for i in wood])
    
    if add == m:
        result = mid
        break
    elif add < m:
        end = mid-1
    elif add > m:
        result = mid
        start = mid+1

print(result)