def solution(i, j, k):
    cnt = 0
    for n in range(i,j+1):
        num = str(n).count(str(k))
        if num:
            cnt+=num
    return cnt