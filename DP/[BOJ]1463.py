n = int(input())
d = [0] * (n + 1)  # d[i] = i번째 수의 최소 연산 횟수
for i in range(2, n + 1):
    findMin = []
    if i % 2 == 0:
        findMin.append(d[i // 2] + 1)
    if i % 3 == 0:
        findMin.append(d[i // 3] + 1)
    findMin.append(d[i - 1] + 1)

    d[i] = min(findMin)
print(d[n])
