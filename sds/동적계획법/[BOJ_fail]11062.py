# dp는 dp로 풀어야한다는 교훈을 얻었다.
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    game = []
    s = 0
    e = n-1
    if n==1:
        print(a[0])
        exit()
    for i in range(n):
        # 양 끝의 카드의 값이 같다면, 안쪽의 카드 값이 작은 것을 택해야 상대보다 점수를 더 많이 가져갈 수 있다.
        if a[s] == a[e]:
            if i == n-1: # 마지막 턴이라면
                game.append(a[s])
                s+=1
            elif a[s+1] >= a[e-1]:
                game.append(a[e])
                e-=1
            else:
                game.append(a[s])
                s+=1
        # 시작 카드의 값이 크지만, 그 카드 안쪽의 값이 마지막 카드의 값보다 크다면 마지막 카드를 택해야 상대보다 점수를 더 많이 가져갈 수 있다.
        elif a[s] > a[e]:
            if a[s+1] > a[s] and a[s+1] > a[e-1]:
                game.append(a[e])
                e-=1
            else:
                game.append(a[s])
                s+=1
        else:
            if a[e-1] > a[e] and a[s+1] < a[e-1]:
                game.append(a[s])
                s+=1
            else:
                game.append(a[e])
                e-=1
    print(sum([game[i] for i in range(0,n,2)]))