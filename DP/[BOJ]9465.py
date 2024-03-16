t = int(input())
for _ in range(t):
    n = int(input())
    a = [[0] for _ in range(3)]
    a[0].extend([0] * n)
    a[1].extend(list(map(int, input().split())))
    a[2].extend(list(map(int, input().split())))

    d = [[0] * (n + 1) for _ in range(3)]

    for i in range(1, 3):
        for j in range(1, n + 1):
            first = a[i][j] + d[i][j - 2] + d[i - 1][j - 1] # 여기에서 문제발생
            second = max(d[i - 1][j], d[i][j - 1])
            d[i][j] = max(first, second)

    print(d[2][n])
