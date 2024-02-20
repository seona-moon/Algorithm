from collections import deque
begin = "hit"
target = "cog"

words = ["hot", "dot", "dog", "lot", "log", "cog"]

def search(wordA, wordB):
    count = 0
    n = len(wordA)
    for i in range(n):
        if wordA[i] == wordB[i]:
            count +=1
    return True if count == n-1 else False
        
def solution(begin, target, words):
    n = len(words)
    visited = [0]*n
    q = deque()
    if target not in words:
        return 0
    
    q.append((begin,0))
    while q:
        # 큐에서 뺀다
        word, answer = q.popleft()
        # 목적지인가?
        if word == target:
            break
        # 순회
        for i in range(len(words)):
            # 갈 수 있는가?
            next = words[i]
            if visited[i]==0 and search(word,next):
                # 체크인
                visited[i]=1
                answer += 1
                q.append((next, answer))
    return answer
    
print(solution(begin,target,words)) # return 4