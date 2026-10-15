def solution(places):
    answer = []
    
    
    # 대기실 하나씩 확인 
    for place in places :
        safe = True
        
        for r in range(5) :
            for c in range(5) :
                if place[r][c] != "P" :
                    continue
                    
                directions = [
                    (-1,0),
                    (1,0),
                    (0,1),
                    (0,-1)
                ]
                
                for dr,dc in directions :
                    nr = r +dr
                    nc = c + dc
                    
                    if nr < 0 or nr >= 5 or nc <0 or nc >= 5 :
                        continue
                        
                    if place[nr][nc] == "P":
                        safe = False
                    
                    directions2 = [
                        (-2,0),
                        (2,0),
                        (0,-2),
                        (0,2)
                    ]
                    
                    for dr,dc in directions2 :
                        nr = r +dr
                        nc = c + dc
                        
                        if nr < 0 or nr>=5 or nc<0 or nc>=5 :
                            continue
                            
                        # 거리가 2인 곳에 p가 있다면
                        if place[nr][nc] == "P":
                            mr = r + dr // 2
                            mc = c + dc // 2
                            
                            if place[mr][mc] != "X":
                                safe = False
                                
                    diagonal = [
                        (-1,-1),
                        (-1,1),
                        (1,-1),
                        (1,1)
                        
                    ]
                    
                    for dr,dc in diagonal :
                        nr = r+dr
                        nc = c+dc
                        
                        if nr <0 or nr >= 5 or nc <0 or nc >= 5 :
                            continue
                            
                        if place[nr][nc] == "P":
                            if place[r][nc] != "X" or place[nr][c] != "X" :
                                safe = False
                                
        if safe :
            answer.append(1)
            
        else :
            answer.append(0)
    return answer
    
    
   