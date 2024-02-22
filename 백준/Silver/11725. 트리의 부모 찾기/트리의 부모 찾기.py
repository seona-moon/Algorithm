from collections import deque

n = int(input())
adj = [[i] for i in range(n+1)] # 연결 리스트로 트리 구현
visited = [0]*(n+1) # 부모의 값을 적어주는 bfs
q = deque()

for _ in range(n-1):
    a, b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

q.append(1)
visited[1] = 1
while q:
    # 갈 수 있는가?
    now = q.popleft()
    for next in adj[now]:
        if not visited[next]:
            visited[next] = now
            q.append(next)

for i in range(2,n+1):
    print(visited[i])