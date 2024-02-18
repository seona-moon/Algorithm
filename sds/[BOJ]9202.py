
class Node(object):
    def __init__(self, key):
        self.child = {}
        self.key = key
        self.isWord = False
        self.isHit = False

class tri:
    def __init__(self):
        self.head = Node(None)
    
    # insert함수 - 트리를 생성하기 위한 함수
    def insert(self, string):
        # head노드부터 시작
        current_node = self.head
        
        # 문자열의 문자를 하나씩 확인
        for char in string:
            # 현재 노드의 자식중에 문자가 없다면
            if char not in current_node.child:
                # 자식 노드 추가 (딕셔너리를 이용)
                current_node.child[char] = Node(char)
            # 자식 중에 문자가 있다면 current_node를 자식 노드로 변경
            current_node = current_node.child[char]
        
        # 문자열을 끝까지 탐색했다면 마지막 노드에 data추가
        current_node.data = string
    
    def hasChild(map[ty][tx]):
        #자식 있는지 확인
        return
    
    # Hit를 초기화하는 함수
    def clearHit(self):
        self.head.isHit = False
        current_child = self.head.child
        for char in current_child:
            if char in current_child:
                current_child.clearHit()

    def search(y, x, length, node):
        # 1. 체크인
        visited[y][x] = True
        #map[y][x] += 1
        
        # 2. 목적지인가? (단어 완성 + 중복 체크)
        if node.isWord == True and node.isHit == False:
            node.isHit = True
            add += score[length]
            count += 1
            # 값을 비교해서 answer이랑 foundWord랑 비교해서 답을 갱신하자
    
        # 3. 연결된 곳을 순회
        for i in range(8):
            ty = y + my[i]
            tx = x + mx[i]
            # 4. 갈 수 있는가? (맵 체크, 방문 체크, 노드가 해당 자식을 가지는지 체크)
            if 0 <= ty and ty < 4 and 0 <= tx and tx < 4:
                if visited[ty][tx] == False and node.hasChild(map[ty][tx]):
                    # 5. 간다
                    search(ty, tx, length+1, node.getChild(map[ty][tx]))
        
        # 6. 체크아웃
        visited[y][x] = False
        #map[y][x] -= 1

mx = [-1, 1, 0, 0, -1, 1, -1, 1]
my = [0, 0, -1, 1, -1, -1, 1, 1]
score = [0, 0, 1, 1, 2, 3, 5, 11]

add = 0
answer = ""
count = 0
root = Node()
map = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
visited = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# 맵 받아오기

# 출력하기 (root기준으로 해당 자식을 가지고 있을 때 시작 가능)
for y in range(4):
    for x in range(4):
        if root.hasChild(map[y][x]):
            search(y, x, 1, root.getChild(map[y][x]))