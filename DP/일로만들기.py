# 정수 X를 입력 받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0]*300001

#d[i] : i번째 수를 계산하는 최소 연산 횟수
for i in range(2,x+1):
    # 현재의 수에서 1을 빼는 경우 (Default)
    d[i] = d[i-1]+1
    # 현재의 수에서 3을 나누는 경우 (최소 연산 횟수를 Min을 통해 계산)
    if i%2==0:
        d[i] = min(d[i//2]+1,d[i])
    if i%3==0:
        d[i] = min(d[i//3]+1,d[i])
    if i%5==0:
        d[i] = min(d[i//5]+1,d[i]) 

print(d[x])