# n,m이 100까지라서 조합은 200의 값이 최대!
d = [[0]*201 for _ in range(201)] # n C r 구현

for i in range(0,201):
    d[i][0] = 1 # n C 0 = 1

# n C r = n-1 C r-1 + n-1 C r -> 파스칼의 삼각형으로 조합 계산
for i in range(1,201):
    for j in range(1,i+1):
        d[i][j] = d[i-1][j-1] + d[i-1][j]

# n이 a, m이 z
n, m, k = map(int, input().split())

s = ''
count = n+m
t = n+m

if d[t][m] < k: print(-1)
else:
    for i in range(count):
        # 첫 문자가 a라고 가정
        t-=1
        comb = d[t][n-1]
        if not m:
            s+='a'
        elif not n:
            s+='z'
        elif comb >= k:
            s+='a'            
            n-=1
        else:
            s+='z'
            k-=comb
            m-=1
    print(s)