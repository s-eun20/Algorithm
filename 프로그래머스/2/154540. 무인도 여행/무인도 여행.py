from collections import deque
def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    
    visited = [[False] * cols for _ in range(rows)]
    answer = []
    
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    for start_r in range(rows) :
        for start_c in range(cols) :
            
            if maps[start_r][start_c] == 'X' :
                continue
            if visited[start_r][start_c] :
                continue
            
            queue = deque()
            queue.append((start_r,start_c))
            visited[start_r][start_c] = True
            
            total = 0
            
            while queue :
                r,c = queue.popleft()
                total += int(maps[r][c])
                
                for i in range(4) :
                    nr = r + dr[i]
                    nc = c + dc[i]
                    
                    if 0<=nr<rows and 0<=nc<cols :
                        if maps[nr][nc] != 'X' and not visited[nr][nc] :
                            visited[nr][nc] = True
                            queue.append((nr,nc))
                        
            answer.append(total)
            
    if not answer :
        return [-1]
    return sorted(answer)