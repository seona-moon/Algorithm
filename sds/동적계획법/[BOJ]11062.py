import sys, heapq

T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    dp = [[0 for _ in range(N)] for _ in range(N)] # dp[i][j] : 카드가 i~j까지 있을 때 최대의 합

    turn = True if N % 2 == 1 else False # True일 때 근우차례

    for size in range(N):
        for i in range(N - size):
            if size == 0:
                dp[i][i+size] = arr[i] if turn else 0
            elif turn: #근우차례 : 선택할 카드(i or j) + 다음에 선택할 카드의 합이 최대가 되도록 선택
                dp[i][i+size] = max(dp[i+1][i+size] + arr[i], dp[i][i+size-1] + arr[i+size])
            else: #명우차례 : 명우의 선택(i or j) 후 남은 카드들로 근우가 선택할 카드의 합이 최소가 되도록 선택
                dp[i][i+size] = min(dp[i+1][i+size], dp[i][i+size-1])
            
        turn = not turn #차례바꿈

    print(dp[0][N-1])