repl = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
# 왼위 왼아 오위 오아
dx = [-1, -1, 1, 1, -2, 2, -2, 2]
dy = [-2, 2, -2, 2, -1, -1, 1, 1]

location = input()
x = int(location[1])
y = repl[location[0]]

cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 9 and nx > 0 and ny < 9 and ny > 0:
        cnt += 1

print(cnt)
