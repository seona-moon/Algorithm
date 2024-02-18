from dataclasses import dataclass

@dataclass
class candidate:
    time: int
    num: int
    count: int
    isIn: bool
    def __init__(self, i):
        self.isIn=False
        self.count=0
        self.num=i
        self.time=0

N = int(input())
M = int(input())
# 추가할 인원
array = list(map(int, input().split()))
#사진틀
pictures = list()
candidates = [0]
for i in range(1,101):
    candidates.append(candidate(i))

for n in array:
    # 이미 사진틀에 올라와있다면?
    if candidates[n].isIn==True:
        candidates[n].count +=1    
    #사진틀에 처음 올라가는 사람이라면?
    if candidates[n].isIn==False:
        #만약 사진틀이 비어있다면? -> 추가

        if len(pictures) < N:
            pictures.append(n)
            candidates[n].isIn = True
        #만약 사진틀이 꽉 차있다면? ->기존 사진 빼서 본인 넣기
        else:
            # 사진틀의 카운트 제일 작은 값 빼기
            minCount = 1001
            minTime = 1001
            flag = False
            for k in pictures:
                # 카운트가 동일한 값이 존재
                if candidates[minCount].count == candidates[k].count:
                    flag = True
                # 카운트가 더 작은 값 존재
                elif candidates[k].count < candidates[minCount].count:
                    flag = False
                    minCount = k
                # 2차 조건을 위해 시간값도 저장
                if candidates[k].time < candidates[minTime].time:
                    minTime = k
            # 카운트가 모두 같다면 -> 가장 time이 작은 값 빼기
            if flag:
                candidates[minTime].isIn = False
                pictures.remove(minTime)
            # 최소 카운트가 있다면 해당 값 제거
            else:
                candidates[minCount].isIn = False
                pictures.remove(minCount)
            
            #본인 사진 넣기
            candidates[n].isIn = True
            pictures.append(n)

print(sorted(pictures))