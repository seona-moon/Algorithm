a = input()
b = input()

d = [[0]*len(b) for _ in range(len(a))]
ans = 0

for pa in range(len(a)):
    for pb in range(len(b)):
        if a[pa] == b[pb]:
            if pa == 0 : d[0][pb] = 1
            elif pb == 0 : d[pa][0] = 1
            else: d[pa][pb] = d[pa-1][pb-1] + 1
            ans = max(ans,d[pa][pb])
print(ans)