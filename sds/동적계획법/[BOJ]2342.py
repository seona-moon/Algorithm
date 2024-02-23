a = list(map(int,input().split()))
foot = [0,0].reverse()
answer = 0



    # order = a[i]
    # if not order: break
    # if i==0:
    #     foot[0] = order
    #     answer += 2
    #     continue
    # # 1. 발의 숫자랑 같은 위치의 명령이 나오면 진행
    # if foot[0]==order or foot[1]==order: answer += 1
    # # 2. 발 중 인접 위치가 존재하면 진행
    # elif abs(foot[0]-order)%2 == 1:
    #     foot[0] = order
    #     answer += 3
    # elif abs(foot[1]-order)%2 == 1:
    #     foot[1] = order
    #     answer += 3
    # # 3. 발이 반대위치라면 아무거나 진행
    # else:
    #     if not foot[0]:
    #         foot[0] = order
    #         answer += 2
    #     elif not foot[1]:
    #         foot[1] = order
    #         answer += 2
    #     if foot[0]==foot[1]:
    #         foot[0] = order
    #         answer += 4