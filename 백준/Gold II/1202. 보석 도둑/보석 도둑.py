import sys
import heapq

class jewel:
    weight: int
    value: int
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

n, m = map(int, sys.stdin.readline().split())
jewels = []
packs = []
for i in range(n):
    weight, value = map(int, sys.stdin.readline().split())
    jewels.append(jewel(weight, value))
for _ in range(m):
    packs.append(int(sys.stdin.readline()))

# 1. 가방을 오름차순 정렬
packs.sort()
# 2. 보석을 무게 순 오름차순 정렬
jewels.sort(key=lambda x: x.weight)

jp = 0
result = 0
posJewel = []
# 3. 작은 가방부터 선택
for pp in range(len(packs)):
    currentPack = packs[pp]

    # 4. 가방에 넣은 수 있는 보석 중 가장 비싼 보석 선택 (힙 사용)
    while (jp < n and jewels[jp].weight <= currentPack):
        heapq.heappush(posJewel, (-jewels[jp].value, jewels[jp].value))
        jp += 1
    if len(posJewel):
        result += heapq.heappop(posJewel)[1]

print(result)