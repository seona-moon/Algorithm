import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

MAX = sys.maxsize
d = [[MAX]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    d[i][i]=0

for _ in range(m):
    s, e, w = map(int, input().split())
    d[s][e] = min(w, d[s][e])

# 플로이드 워셜
# 1~n개의 모든 점을 지나면서 최솟값을 업데이트
for k in range(1,n+1): # 지나는 점
    for i in range(1,n+1): # 시작점
        for j in range(1,n+1): # 끝점
            # i > j로 가는 길보다 i > k > j로 가는 길이 더 최소이면 업데이트!
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

# 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        if d[i][j]==MAX:
            print(0,end=" ")
        else: print(d[i][j],end=" ")
    print()