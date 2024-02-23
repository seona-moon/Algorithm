n, m = map(int,input().split())
memory = list(map(int,input().split()))
cost = list(map(int,input().split()))
memory.insert(0,0)
cost.insert(0,0)

tCost = sum(cost)

# d[i][c] : 현재 메모리 한도가 c일때, i번째 앱을 종료하는 최대의 확보 메모리
d = [[0]*(tCost+1) for _ in range(n+1)]

for i in range(n+1):
    for c in range(tCost+1):
        if i==0: break # 앱을 종료하지 않는 경우는 확보 메모리 X
        if c < cost[i]: 
            d[i][c] = d[i-1][c]
        elif c >= cost[i]:
            d[i][c] = max(memory[i] + d[i-1][c-cost[i]], d[i-1][c])

for c in range(tCost+1): 
    if d[n][c] >= m: 
        print(c)
        break