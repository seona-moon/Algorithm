n = int(input()) #2*n 직사각형
d = [0]*(n+1) # d[i] = 2*i 타일 채우는 방법의 수
d[0] = 1
d[1] = 1

for i in range(2,n+1):
    # 덧붙이는 타일이 1개짜리 or 2개짜리
    d[i] = d[i-1]+d[i-2]

print(d[n]%10007)