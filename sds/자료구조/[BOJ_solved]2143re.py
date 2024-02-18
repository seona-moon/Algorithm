from collections import defaultdict
import sys
input = sys.stdin.readline()

t = int(input)
n = int(input)
A = list(map(int,input.split()))
m = int(input)
B = list(map(int,input.split()))

# 각 부분합의 카운트를 계산하기 위해 dict선언 (key:부분합, value:개수)
subDict = defaultdict(int)
result = 0
# A의 부분합 추가
for i in range(n):
    for j in range(i,n):
        subDict[sum(A[i:j+1])] += 1
# B의 부분합 추가 및 계산
for i in range(m):
    for j in range(i,m):
        result += subDict[t-sum(B[i:j+1])] # T - B부분합 = A부분합 << 일때, 조건 만족. 해당하는 케이스 더함

print(result)