def solution(board, moves):
    answer = 0
    basket = []
    
    for move in moves :
        for i in range(len(board)) :
            
            #인형 발견 
            if board[i][move-1] != 0 :
                doll = board[i][move-1]
                board[i][move-1] = 0
                
                if basket and basket[-1] == doll :
                    answer += 2
                    basket.pop()
                    
                else :
                    basket.append(doll)
                    
                    
                break
                
                
        
    return answer


# 뽑을 땐 stack