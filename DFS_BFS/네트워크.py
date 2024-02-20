from collections import deque

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]] # return 2
visited =  [0]*n
q = deque()

def solution(n, computers):
    answer = 0
    
    for i in range(n):
        if visited[i] == 0:
            q.append(i)
            visited[i]=1
            while q:
                # 큐에서 뺀다
                now = q.popleft()
                # 갈 수 있는가?
                for i in range(n):
                    if i==now: continue
                    if computers[now][i]==1 and visited[i]==0:
                        q.append(i)
                        visited[i]=1
        else: continue
        answer += 1
    
    return answer

print(solution(n, computers))