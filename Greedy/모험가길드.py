N = input()
horror = list(map(int, input().split()))
horror.sort()
cnt = 0
result = 0

for i in horror:
    cnt += 1  # 모험가의 수
    if cnt >= i:  # 만약 그룹 내 모험가의 수가 현재 공포도보다 크거나 같으면
        result += 1
        cnt = 0
print(result)
