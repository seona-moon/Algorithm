def solution(n):
    cnt = 0
    answer = 0
    while(cnt!=n):
        answer += 1
        if answer%3==0 or str(answer).count("3"):
            continue
        cnt += 1
    return answer
        