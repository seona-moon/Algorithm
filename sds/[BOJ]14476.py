# def gcd_recur(a,b):
#     if a%b==0:
#         return b
#     return gcd_recur(b, a%b)

def gcd(a,b):
    # gcd(a,b) == gcd(b, a%b)
    while(b!=0):
        r = a%b
        a, b = b, r
    return a

n = int(input())
num = list(map(int,input().split()))
gcdLtoR= [0]*n
gcdRtoL= [0]*n

gcdLtoR[0]=num[0]
for i in range(1,n):
    # gcd(a,b,c) == gcd((a,b),c): 해당 원리를 이용함
    gcdLtoR[i] = gcd(gcdLtoR[i-1], num[i])

gcdRtoL[n-1]=num[n-1]
for i in range(0,n-2,-1):
    gcdRtoL[i] = gcd(gcdRtoL[i+1], num[i])

result = 0
k = 0
for i in range(n):
    maxGcd = 0
    if i == 0:
        maxGcd = gcdRtoL[1]
    elif i == n-1:
        maxGcd = gcdLtoR[n-2]
    else:
        maxGcd = gcd(gcdLtoR[i-1], gcdRtoL[i+1])
    
    if maxGcd>result:
        result = max(result,maxGcd)
        k = num[i]

# 문자 + 숫자 연결 다시
print(str(result)+" "+k if k!=0 else 0)