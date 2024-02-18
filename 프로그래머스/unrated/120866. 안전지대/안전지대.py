def search(board, x, y):
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if 0<=i<len(board) and 0<=j<len(board):
                if board[i][j]==0:
                    board[i][j] = -1 #위험지역

def solution(board):
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y]==1: #지뢰지역
                search(board, x, y)
    
    return sum(e.count(0) for e in board)