money = (500, 100, 50, 10)
change = int(input())
cnt = 0

for i in money:
    cnt += change // i
    change %= i
print(cnt)
