def solution(sizes):
    # 항상 큰 값을 가로, 작은 값을 세로에 맞춘다
    
    max_width = 0
    max_height = 0
    
    for w,h in sizes :
        
        # 큰 값을 가로
        if w < h :
            w,h = h,w
            
        max_width = max(max_width,w)
        max_height = max(max_height,h)
        
    return max_width * max_height