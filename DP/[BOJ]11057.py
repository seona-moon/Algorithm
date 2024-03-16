n = int(input())  # 길이가 N인 오르막 수 찾기
d = [[0] * 10 for _ in range(n + 1)]  # sum(d[i]) = i번째 오르막수의 합

for i in range(10):
    d[1][i] = 1
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i - 1][j]
        else:
            d[i][j] = sum(d[i - 1][: j + 1])  # 본인보다 작거나 같은 수의 합

print(sum(d[n]) % 10007)
