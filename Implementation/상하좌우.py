# LRUD
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
order_mean = {"L": 0, "R": 1, "U": 2, "D": 3}

N = int(input()) + 1
order = list(input().split())
x, y = 1, 1

for i in order:
    nx = x + dx[order_mean[i]]
    ny = y + dy[order_mean[i]]

    if nx > 0 and ny > 0 and nx <= N and ny <= N:
        x = nx
        y = ny

print([x, y])
