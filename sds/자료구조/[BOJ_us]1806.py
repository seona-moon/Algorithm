import sys

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
start, end = 0, 0
length = 10001

while(end<n):
    add = 0
    for i in range(start,end):
        add += array[i]
    currentLength = end-start+1
    
    if add >= m:
        if start == end:
            length = 1
            break
        start += 1
        length = min(currentLength,length)
    elif add < m:
        end += 1

print(length if length!=10001 else 0)