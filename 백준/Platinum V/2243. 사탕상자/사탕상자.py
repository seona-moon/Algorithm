import sys
# n번째로 맛있는 사탕의 맛을 찾는다
def search(left, right, node, target):
    if left==right:
        return left
        
    mid = (left+right)//2
    leftNode = node*2
    rightNode = node*2+1
    
    # 왼쪽으로 이동
    if tree[leftNode] >= target:
        return search(left,mid,leftNode,target)
    # 오른쪽으로 이동
    else:
        target -= tree[leftNode]
        return search(mid+1,right,rightNode,target)
        
    
# 특정 맛의 사탕을 넣거나 뺀다
def update(left, right, node, target, diff):
    # target = 사탕 맛
    if right < target or left > target:
        return
    else:
        tree[node] += diff
        # 자식이 있는지 판단
        if left!=right:
            mid = (left+right)//2
            update(left,mid,node*2,target,diff)
            update(mid+1,right,node*2+1,target,diff)
            
n = int(sys.stdin.readline())
# 빈 사탕상자로 초기화

#S 계산하기
s = 1
while(s<1000000):
    s *= 2

tree = [0]*(s*2)

for _ in range(n):
   answer =  list(map(int,sys.stdin.readline().split()))
   # A가 1인 경우는 사탕상자에서 사탕을 꺼내는 경우이다. 이때에는 한 정수만 주어지며, B는 꺼낼 사탕의 순위를 의미한다. 
   # 이 경우 사탕상자에서 한 개의 사탕이 꺼내지게 된다.
   if answer[0]==1:
       flavor = search(1,s,1,answer[1]) # 꺼낼 사탕의 맛 찾기
       update(1,s,1,flavor, -1)
       print(flavor)
   else:
       update(1,s,1,answer[1], answer[2])
   # A가 2인 경우는 사탕을 넣는 경우이다. 이때에는 두 정수가 주어지는데, B는 넣을 사탕의 맛을 나타내는 정수이고 
   # C는 그러한 사탕의 개수이다. C가 양수일 경우에는 사탕을 넣는 경우이고, 음수일 경우에는 빼는 경우이다.

