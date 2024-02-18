n, m = map(int,input().split())
array = list(map(int,input().split()))
ans = 0
low, high= 0, 0

#투포인터로 서칭 시작
while(high<n):
    add = sum(array[low:high+1])
    
    if add > m:
        low += 1
    elif add < m:
        high += 1
    elif add == m:
        ans += 1
        high += 1

print(ans)
    
