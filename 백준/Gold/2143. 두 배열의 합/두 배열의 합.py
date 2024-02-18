import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

def makeSub(n,arr):
    array = []
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            array.append(sum)
    return array

sumA = makeSub(n,A)
sumB = makeSub(m,B)

sumA.sort()
sumB.sort(reverse=True)

# 투 포인터
pa, pb = 0, 0
result = 0

while(pa<len(sumA) and pb<len(sumB)):
    add = sumA[pa] + sumB[pb]
    if add > t:
        pb += 1
    elif add < t:
        pa += 1
    else:
        cntA = 0
        cntB = 0
        for i in range(pa,len(sumA)):
            if sumA[pa] == sumA[i]:
                cntA +=1
            else:
                break
        for j in range(pb,len(sumB)):
            if sumB[pb] == sumB[j]:
                cntB +=1
            else:
                break
        result += cntA*cntB
        pa += cntA
        pb += cntB

print(result)