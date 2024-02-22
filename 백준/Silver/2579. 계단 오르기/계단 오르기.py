n = int(input())

a = []
d = [0]*(n+1)

# 계산 리스트
a.append(0)
for _ in range(n):
    a.append(int(input()))

if n==1:
    print(a[1])
elif n==2:
    print(a[1]+a[2])
else:
    # DP 채우기
    d[1] = a[1]
    d[2] = d[1]+a[2]
    for i in range(3,n+1):
        d[i] = a[i] + max(a[i-1]+d[i-3], d[i-2])

    print(d[n])