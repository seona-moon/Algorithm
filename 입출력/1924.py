DAY = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
a, b = map(int, input().split())
sum = 0
for i in range(1, a):  # 1~a-1 달까지 날짜 계산
    if i in [1, 3, 5, 7, 8, 10, 12]:
        sum += 31
    elif i == 2:
        sum += 28
    else:
        sum += 30
sum += b

print(DAY[sum % 7])
