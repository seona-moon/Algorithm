def solution(sides):
    answer = 0
    mini, maxi = min(sides), max(sides)
    # max가 가장 긴 변 + answer이 가장 긴 변
    for e in range(1,maxi+mini):
        if e <= maxi:
            answer += 1 if maxi < mini+e else 0
            continue
        answer+= 1 if e < mini+maxi else 0
            
    return answer