def solution(park, routes):
    # 시작 위치 찾기
    x,y = 0,0
    
    for i in range(len(park)) :
        for j in range(len(park[i])) :
            if park[i][j] == "S" :
                x,y = i,j
    
    direction = {
        "E" : (0,1),
        "W" : (0,-1),
        "S" : (1,0),
        "N" : (-1,0)
    }
    
    for route in routes :
        
        op,n = route.split()
        n = int(n)
        
        dx,dy = direction[op]
        
        nx,ny = x,y # 시작점
        
        can_move = True
        
        #한 칸씩 이동 확인
        
        for _ in range(n) :
            
            nx += dx
            ny += dy
            
            if not (0<=nx<len(park) and 0 <= ny < len(park[0])) :
                can_move = False
                break
                
            # 장애물 체크
            if park[nx][ny] == "X":
                can_move=False
                break
                
        #이동 가능하면 최종 위치 갱신
        if can_move :
            x,y = nx,ny
            
    return [x,y]