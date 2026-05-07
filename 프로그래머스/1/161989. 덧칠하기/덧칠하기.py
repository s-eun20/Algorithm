def solution(n, m, section):
    count = 0
    painted = 0
    
    for s in section :
        
        # 아직 안 칠해진 경우
        if painted < s :
            count += 1
            
            # 이번에 칠한 마지막 위치 
            painted = s + m -1
        
    return count