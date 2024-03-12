n = int(input())
info = []
for i in range(n):
    x, y = input().split()
    info.append([int(x), y, int(i)])

info.sort(key=lambda x: (x[0], x[2]))
for i in range(n):
    print(info[i][0], info[i][1])
