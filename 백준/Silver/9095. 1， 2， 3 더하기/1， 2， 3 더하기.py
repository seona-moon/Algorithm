t = int(input())
d = [0] * (11)
d[0] = 1
d[1] = 1
d[2] = 2
for i in range(3, 11):
    # d[i] = 1,2,3을 덧붙이는 경우 더하기
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]
for _ in range(t):
    n = int(input())
    print(d[n])
