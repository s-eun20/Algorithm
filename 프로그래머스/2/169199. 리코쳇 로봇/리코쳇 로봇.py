from collections import deque
def solution(board):
    rows = len(board)
    cols = len(board[0])
    
    for r in range(rows) :
        for c in range(cols) :
            if board[r][c] == "R" :
                start_r,start_c = r,c
    # 상하좌우
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    distance = [[-1] * cols for _ in range(rows)]
    queue = deque([(start_r,start_c)])
    distance[start_r][start_c] = 0
    
    while queue :
        r,c = queue.popleft()
        
        if board[r][c] == "G" :
            return distance[r][c]
        
        for dr,dc in directions :
            nr,nc = r,c
            
            # 벽이나 장애물을 만날 때 까지 계속 이동
            while True :
                next_r = nr + dr
                next_c = nc + dc
                
            # 범위를 벗어나면 현재 위치에서 멈춤
                if not (0<=next_r<rows and 0<=next_c<cols) :
                    break
                
            # 장애물 D면 현재 위치에서 멈춤
                if board[next_r][next_c] == "D" :
                    break
                nr = next_r
                nc = next_c
            
        # 움직이지 않은 경우
            if nr == r and nc == c :
                continue
        
        # 처음 방문한 정지 지점이면 큐에 추가
            if distance[nr][nc] == -1 :
                distance[nr][nc] = distance[r][c] + 1
                queue.append((nr,nc))
        
    return -1