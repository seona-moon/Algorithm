import sys
input = sys.stdin.readline

n, m = map(int,input().split())

d = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    d[s][e] = 1

# 플로이드 워셜
# 1~n개의 모든 점을 지나면서 업데이트
for k in range(1,n+1): # 지나는 점
    for i in range(1,n+1): # 시작점
        for j in range(1,n+1): # 끝점
            # i > k > j로 가는 길이 있다면 비교 가능
            if d[i][k] and d[k][j]:
                d[i][j] = 1

# 출력
result = 0
for i in range(1,n+1):
    count = 0
    for j in range(1,n+1):
        if d[i][j]:
            count += 1
        if d[j][i]:
            count += 1
    if count == n-1:
        result += 1
print(result)