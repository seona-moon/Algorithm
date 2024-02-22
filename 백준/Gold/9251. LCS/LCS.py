a = input()
b = input()

# d = i,j까지의 최장 증가 수열의 길이
d = [[0]*(len(b)+1) for _ in range(len(a)+1)]
ans = 0
s = ''
for pa in range(1,len(a)+1):
    for pb in range(1,len(b)+1):
        if a[pa-1] == b[pb-1]:
            d[pa][pb] = d[pa-1][pb-1] + 1
        else:
            d[pa][pb] = max(d[pa][pb-1],d[pa-1][pb-1],d[pa-1][pb])
        

print(d[len(a)][len(b)])