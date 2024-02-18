import math
# X = 인 당 나눠줄 사탕의 수
# Y = 사탕 봉지의 수 (C)

# A*X + 1 = B*Y
# Ax + By = C 의 형태로 벼환
# -Ax + By = 1

# A와 B가 항상 양수가 되어야 함 (정수론 개념이랑 컴퓨터 개념이 달라서)
# A(-x) + By = 1 (나중에 답 구하고 -만 곱해주면 됨!)

# As + Bt = r을 만족하는 s,t,r구하는 과정
def egcd(a, b):
    s0, t0, r0 = 1, 0, a
    s1, t1, r1 = 0, 1, b
    
    # gcd 계산
    temp = 0
    while(r1 != 0):
        q = r0//r1
        # 확장 유클리드 호제법
        r0, r1 = r1, r0 - q*r1
        s0, s1 = s1-s0, s0 - q*s1
        t0, t1 = t1-t0, t0 - q*t1
    
    EGResult.append({s0, t0, r0})
    return {s0, t0, r0}

# 클래스나 배열로 구현하는 것은 마음대로 하면 됨.
EGResult = []

t = input()
A, B = map(int, input().split())
result = egcd(A,B)


# D = gcd(A,B) = 1이므로 생략
# Ax + By = C 일때, C % D == 0 이어야만 해를 가질 수 있다. (베주 항등식)
if result[2] != 1: # 1 % result.r !==0
    # 해가 없음
    print("IMPOSSIBLE")
else:
    # x0 = s * C/D
    # y0 = t * C/D
    s, t = result[0], result[1]
    x0 = s
    y0 = t
    
    # 일반해 공식 (무수한 해 중에 하나를 찾는 방법)
    # x = x0 + (B/D)*K (K는 상수)
    # y = y0 - (A/D)*K (이때, 초기에 A(-x)였기에 부호 반대)
    
    # x < 0 (부호 반대)
    # x0 = B * K < 0 (D=1이므로 생략)    
    # K < - x0 / B
    
    # 0 < y < 1e9
    # 0 < y0 - A * K <= 1e9
    # -y0 < - A * K <= 1e9
    # (y0 - 1e9) / A <= K < y0 / A
    
    # 최종적으로 k의 범위가 다음과 같다. 
    # (y0 - 1e9) / A <= K < y0 / A
    #                   K < - x0 / B
    # K < min(y0/A, -x0/B) 이때, 해당 K가 (y0 - 1e9) / A보다 작다면 만족하는 해가 없다고 생각하기!
    
    # (y0 - 1e9) / A <= K < y0 / A
    kFromY = math.ceil((y0/A))-1
    # K < - x0 / B
    kFromX = math.ceil((x0/B))-1
    k = min(kFromX,kFromY)
    # 이때, y0 / A는 단순히 정수형으로 바꾸는게 아니라, 올림을 한 후 -1을 빼야 나온다. (조심. 기억하기!)
    # 만약 등호가 있으면 내림을 하고 +1을 해야 나온다! (실제로 숫자를 써보면서 케이스별로 생각해보기)
    
    # (y0 - 1e9) / A <= K
    kLimitFromY = math.ceil((y0-1e9)/A)
    if kLimitFromY <= k:
        # 해가 존재 (아니면 없음)
        print(y0 - A*k)
    else:
        print("IMPOSSIBLE")