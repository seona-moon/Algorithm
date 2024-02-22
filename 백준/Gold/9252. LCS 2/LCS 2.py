a = input()
b = input()

# d = i,j까지의 최장 증가 수열의 길이
d = [[0]*(len(b)+1) for _ in range(len(a)+1)]
for pa in range(1,len(a)+1):
    for pb in range(1,len(b)+1):
        if a[pa-1] == b[pb-1]:
            d[pa][pb] = d[pa-1][pb-1] + 1
        else:
            d[pa][pb] = max(d[pa][pb-1],d[pa-1][pb-1],d[pa-1][pb])
print(d[len(a)][len(b)])

s = ''
cnt = d[len(a)][len(b)]
if cnt == 0:
    exit()
flag = False
for pa in range(len(a),0,-1):
    if flag: break
    for pb in range(len(b),0,-1):
        if cnt==0:
            flag = True
            break
        if d[pa][pb] < cnt: break
        if d[pa][pb]==cnt and max(d[pa][pb-1],d[pa-1][pb-1],d[pa-1][pb])== (cnt-1):
            s += a[pa-1]
            cnt -=1
            break
print(s[::-1])