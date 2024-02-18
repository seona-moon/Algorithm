import sys

# Bottom Up으로 초기화!
def init(tree):
    for i in range(s):
        if i < n:
            tree[s+i] = int(nums[i])
        else: break
        i+=1
    #i가 역순으로 돌아야함!
    for j in range(s-1,0,-1):
        #부모 = 왼쪽+아래쪽
        tree[j] = tree[j*2] + tree[j*2+1]

# 문제 풀 때, 케이스에 대한 그림을 그리면서 풀어야 함! (3가지 케이스 생각)
def query(left, right, node, queryLeft, queryRight):
    # 1. 쿼리 범위 밖
    if queryRight < left or right < queryLeft:
        # 리턴값은 로직에 영향을 안주는 수 (구간합 = 0, 구간곱 = 1 등...)
        return 0
    # 2. 쿼리 안에 다 겹침
    if queryLeft <= left and right <= queryRight:
        # 노드 값 온전히 사용
        return tree[node]
    # 3. 애매하게 걸쳐진 값 (자식에게 위임)
    mid = (left+right)//2
    # 왼쪽 + 오른쪽 비교 후 부모에게 전달
    return query(left, mid, node*2, queryLeft, queryRight) + query(mid+1, right, node*2+1, queryLeft, queryRight)

# 이것도 트리 그림을 그려놓고 시작하기
def queryBU(queryLeft, queryRight):
    # s가 시작위치
    leftNode = s+queryLeft-1
    rightNode = s+queryRight-1
    sum = 0
    
    while(leftNode<=rightNode):
        # 왼쪽 노드가 짝수 : 본인 값 계산
        if leftNode%2==1:
            sum += tree[leftNode]
            leftNode += 1
        if rightNode%2==0:
            sum += tree[leftNode]
            rightNode -= 1
        leftNode //= 2
        rightNode //= 2
    return sum

# TopDown은 diff로 움직인다!
# 여기도 그림 그리면서 풀기! (타겟에 해당 x, 타겟에 겹침)
def update(left, right, node, target, diff):
    # 타겟과 무관
    if target > right or target < left:
        return
    # 타겟과 연관
    else:
        # 자기 자신 갱신
        tree[node] += diff
        # 리프가 아닐때 내려감
        if left != right:
            mid = (left+right)//2
            update(left, mid, node*2, target, diff)
            update(mid+1, right, node*2+1, target, diff)

def updateBU(target, value):
    node = s+target-1
    tree[node] = value
    node /= 2
    while(node > 0):
        tree[node] = tree[node*2] + tree[node*2+1]
    node /= 2


n, m, k = map(int, sys.stdin.readline().split())
nums = []
for _ in range(n):
   nums.append(sys.stdin.readline())

# S 계산하기
s = 1
while(s<n):
    s *= 2

tree = [0]*(2*s)
init(tree)

for _ in range(m+k):
    a,b,c = map(int, sys.stdin.readline().split())
    # b(1 ≤ b ≤ N)번째 수를 c로 바꾸기
    if a==1:
        diff = c - tree[s+b-1]
        update(1,s,1,b,diff)
    # a가 2인 경우에는 b(1 ≤ b ≤ N)번째 수부터 c(b ≤ c ≤ N)번째 수까지의 합을 구하여 출력
    elif a==2:
        print(query(1,s,1,b,c))
