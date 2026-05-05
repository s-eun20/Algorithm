def solution(board, h, w):
    count = 0
    n = len(board)
    
    #상하좌우
    dh = [-1,1,0,0]
    dw = [0,0,-1,1]
    
    for i in range(4) :
        nh = h + dh[i]
        nw = w + dw[i]
        
        if 0 <= nh < n and 0 <= nw < n :
            if board[nh][nw] == board[h][w] :
                count += 1
                
    return count 