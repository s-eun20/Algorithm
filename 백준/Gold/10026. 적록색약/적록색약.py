import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,color,grid,visited,n) :
    queue = deque([(x,y)])
    visited[x][y] = True
    
    while queue :
        x,y = queue.popleft()
        
        for i in range(4):
            nx,ny = x + dx[i],y+dy[i]
            
            if 0 <= nx <n and 0 <= ny <n and not visited[nx][ny]:
                if grid[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    
def count_regions(grid,n):
    visited = [[False] * n for _ in range(n)]
    
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i,j,grid[i][j],grid,visited,n)
                count+=1
    return count


def solution():
    n = int(sys.stdin.readline().strip())
    grid = [list(sys.stdin.readline().strip()) for _ in range(n)]
    
    normal_count = count_regions(grid,n)
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'G' :
                grid[i][j] = 'R'
                
                
    colorblind_count = count_regions(grid,n)
    
    print(normal_count, colorblind_count)
    
    
solution()