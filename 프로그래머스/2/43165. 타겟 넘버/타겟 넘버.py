answer = 0

def DFS(idx, numbers, target, value):
    global answer
    # 1. 체크인 (여기에서는 방문 순서가 순차로 결정되어있으므로 visited 생략)
    N = len(numbers)
    # 2. if 목적지인가? (n개의 숫자 순회 완료)
    if(idx == N and target == value):
        answer += 1
        return
    if(idx == N):
        return
    # 3. else 연결된 곳을 순회
    # 	4. 갈 수 있는가?
    # 	5. 간다
    # 각 노드의 합과 차를 둘 다 계산
    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
    
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer