def solution(k, m, score):
    score.sort()
    size = len(score)
    result = 0
    
    for i in range(size%m,size,m):
        result += m*score[i]    
    return result