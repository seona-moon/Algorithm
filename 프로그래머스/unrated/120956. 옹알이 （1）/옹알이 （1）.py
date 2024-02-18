def solution(babbling):
    babble = ["aya", "ye","woo","ma"]
    cnt = 0
    for txt in babbling:
        for rmv in babble:
            txt=txt.replace(rmv," ")
        if len(txt.strip())==0:
            cnt+=1
    return cnt