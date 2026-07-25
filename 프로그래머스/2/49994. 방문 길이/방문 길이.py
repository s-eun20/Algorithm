def solution(dirs):
    x,y = 0,0
    visited = set()
    
    move = {
        "U" : (0,1),
        "D" : (0,-1),
        "L" : (-1,0),
        "R" : (1,0)
    }
    
    for direction in dirs :
        dx,dy = move[direction]
        nx = x + dx
        ny = y + dy
        
        if nx < -5 or nx > 5 or ny < -5 or ny > 5 :
            continue
        path = ((x,y),(nx,ny))
        reverse_path = ((nx,ny),(x,y))
        
        visited.add(path)
        visited.add(reverse_path)
        
        x,y = nx,ny
        
    return len(visited) // 2