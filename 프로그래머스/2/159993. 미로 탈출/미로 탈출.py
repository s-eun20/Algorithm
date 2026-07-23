from collections import deque
def bfs(maps, start_r, start_c, target) :
    rows = len(maps)
    cols = len(maps[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    visited = [[False]*cols for _ in range(rows)]
    queue = deque([(start_r,start_c,0)])
    visited[start_r][start_c] = True
    while queue :
        r,c,dist = queue.popleft()
        
        if maps[r][c] == target :
            return dist
        for dr,dc in directions :
            nr = r +dr
            nc = c+dc
            
            if not (0<=nr<rows and 0<=nc<cols) :
                continue
            if visited[nr][nc] :
                continue
                
            if maps[nr][nc] == "X":
                continue
                
            visited[nr][nc] = True
            queue.append((nr,nc,dist+1))
    return -1
def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    
    for r in range(rows) :
        for c in range(cols) :
            if maps[r][c] == "S" :
                start_r,start_c = r,c
            elif maps[r][c] == "L" :
                lever_r,lever_c = r,c
    
            
    dist1 = bfs(maps,start_r,start_c,"L")
    if dist1 == -1 :
        return -1
    dist2 = bfs(maps,lever_r,lever_c,"E")
    if dist2 == -1:
        return -1
    
    return dist1 + dist2
    
    answer = 0
    return answer