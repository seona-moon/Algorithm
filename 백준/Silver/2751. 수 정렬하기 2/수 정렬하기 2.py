# N(1 ≤ N ≤ 1,000,000) : 힙 사용 
import heapq

n = int(input())
num = []

for _ in range(n):
    heapq.heappush(num, int(input()))

for i in range(n):
    print(heapq.heappop(num))
