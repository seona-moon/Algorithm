import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
count = 1
visited = [0]*(n+1)
lows = [0]*(n+1)
isCut = [False]*(n+1)
adj = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)

def dfs(now, isRoot): 
    global count
    #체크인 (방문 순서 visited에 기록 + low값 계산 - 초깃값은 자기자신)
    count += 1
    visited[now] = count
    low = visited[now] # 인접한 노드 중에 가장 빨리 방문되는 순서
    
    child = 0 #해당 노드의 자식 노드 개수
    for i in range(len(adj[now])):
        next = adj[now][i]

        if visited[next] == 0: # 방문하지 않은 곳 -> dfs 계산
            child += 1
            # lowChild :자식 노드가 갈 수 있는 노드 중에 가장 일찍 방문한 노드의 순번
            lowChild = dfs(next,False) #이후 호출되는 값은 루트가 아니기에 False
            
            # 루트가 아니면서 하위노드의 로우값보다 자신의 방문순서가 더 작으면? 단절점
            if not isRoot and visited[now] <= lowChild: 
                isCut[now] = True
            
            low = min(low,lowChild) # 자기자신의 로우값과 자식의 로우값을 비교해서 작은 값으로 세팅
        
        else: # 방문한 곳 (visited의 방문 순서와 비교)
            low = min(low,visited[next]) # 방문한 곳이라도, 해당 값을 확인해줘야함!!
        
        lows[now] = low

    if isRoot and child >=2: isCut[now] = True #본인이 루트일 때, 자식이 2개 이상이라면? 단절점
    
    return low

# DFS 돌리기
for i in range(1,n):
    if visited[i] == 0:
        dfs(i,True) # 첫번째 노드는 루트

# 출력
cnt = 0
for i in range(n+1):
    if isCut[i]: cnt += 1
print(cnt)
for i in range(n+1):
    if isCut[i]: print(i,end=" ")