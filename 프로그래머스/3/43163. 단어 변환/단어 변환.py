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
    if target not in words:
        return 0
    # 탐색 시작할 인덱스 찾기
    answer = []
    
    def dfs(word, value):
        # 목적지인가?
        if word == target:
            return answer.append(value)
        
        # 순회
        for i in range(len(words)):
            # 갈 수 있는가?
            next = words[i]
            if visited[i]==0 and search(word,next):
                # 간다
                # 체크인
                visited[i]=1
                value += 1
                dfs(next, value)
                # 체크아웃
                visited[i] = 0
                value -= 1
    dfs(begin,0)
    return min(answer)