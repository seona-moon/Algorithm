n, m = map(int,input().split())
a = [0]
for i in range(n):
    a.append(list(map(int,input().split())))

# d[i][j] : 물건을 i개 넣었을 때의 최적의 가치
d = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1): # i번째 물건
    for w in range(1,m+1): # 무게
        #현재 무게가 i번째 보석을 담을 수 없다면 -> 안담는다.
        if w < a[i][0]: 
            d[i][w] = d[i-1][w]
        # 만약 담을 수 있을 때 최적해를 비교!
        # i번째 물건을 담을 공간을 마련한 후 담았을 때의 가치 vs 담지 않았을 때의 가치 비교
        elif w >= a[i][0]: 
            d[i][w] = max(a[i][1]+d[i-1][w-a[i][0]], d[i-1][w])
print(d[n][m])